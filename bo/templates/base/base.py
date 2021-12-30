from flask import Blueprint, render_template, request, redirect, url_for, after_this_request
from flask_login import login_required, current_user
import flask_login
from sqlalchemy.orm import session
from sqlalchemy.sql.functions import current_user, session_user
from bo.models import *
from bo import db, photos
import datetime

base = Blueprint("views", __name__)

@base.route("/")
@base.route("/home")
@login_required
def home():
    return render_template("base/home.html", user=User)

@base.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        updateusr = db.session.query(User).filter(User.id == flask_login.current_user.id).first()
        updateusr.firstname = request.form.get('firstname')
        updateusr.lastname = request.form.get('lastname')
        updateusr.email = request.form.get('email')
        updateusr.username = request.form.get('username')
        updateusr.address = request.form.get('address')
        updateusr.city = request.form.get('city')
        updateusr.state = request.form.get('state')
        updateusr.zip = request.form.get('zip')
        updateusr.phone = request.form.get('phone')
        updateusr.dob = datetime.datetime.strptime(request.form.get('dob'),"%m/%d/%Y")
        filename = photos.save(request.files['avatar'])
        updateusr.avatar_filename = filename
        db.session.commit()
        return render_template('base/home.html')

    states = db.session.query(States).all()
    usr = db.session.query(User).filter(User.id == flask_login.current_user.id).first()
    return render_template("base/profile.html", user=User, usr=usr, states=states)