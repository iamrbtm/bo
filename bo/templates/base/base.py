from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    after_this_request,
    flash,
)
from flask_login import login_required, current_user
import flask_login
from sqlalchemy.orm import session
from bo.models import *
from bo.templates.base.base_process import *
from bo import db, photos
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

base = Blueprint("base", __name__)


@base.route("/")
@base.route("/home")
@login_required
def home():
    return render_template("base/home.html", user=User)


@base.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        updateusr = (
            db.session.query(User)
            .filter(User.id == flask_login.current_user.id)
            .first()
        )
        updateusr.firstname = request.form.get("firstname")
        updateusr.lastname = request.form.get("lastname")
        updateusr.email = request.form.get("email")
        updateusr.username = request.form.get("username")
        updateusr.address = request.form.get("address")
        updateusr.city = request.form.get("city")
        updateusr.state = request.form.get("state")
        updateusr.zip = request.form.get("zip")
        updateusr.phone = request.form.get("phone")
        updateusr.dob = datetime.datetime.strptime(request.form.get("dob"), "%m/%d/%Y")
        filename = photos.save(request.files["avatar"])
        updateusr.avatar_filename = filename
        db.session.commit()
        return render_template("base/home.html")

    states = db.session.query(States).all()
    usr = db.session.query(User).filter(User.id == flask_login.current_user.id).first()
    return render_template("base/profile.html", user=User, usr=usr, states=states)


@base.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        token = get_reset_token(user.id)
        send_reset_email(user.email, token)
        flash(
            "An email has been sent with instructions to reset your password.", "info"
        )
        return redirect(url_for("auth.login"))
    return render_template("base/reset_request.html", user=User)


@base.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if request.method == "POST":
        user = verify_reset_token(token)
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 == password2:
            if user is None:
                flash("That is an invalid or expired token", "warning")
                return redirect(url_for("base.reset_request"))
            else:
                hashed_password = generate_password_hash(password1, method="sha256")
                user.password = hashed_password
                db.session.commit()
                flash(
                    "Your password has been updated! You are now able to log in",
                    "success",
                )
                return redirect(url_for("auth.login"))
        else:
            flash("Password don't match!  Try again!", category="error")

    return render_template("base/reset_token.html", title="Reset Password", user=User)
