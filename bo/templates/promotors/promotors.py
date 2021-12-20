from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from flask_login.utils import login_required
from bo.models import *
from bo.templates.promotors.promotors_process import *


promotor = Blueprint("promotor", __name__)

@promotor.route("/", methods=["GET", "POST"])
@login_required
def promotorlist():
    if request.method == "POST":
        all = request.form.to_dict()
        promotor_add(**all)
    promotorresults = db.session.query(Promotors).all()
    states = db.session.query(States).all()
    cities = db.session.query(Promotors.city).order_by(Promotors.city).distinct()
    context = {
        "user": User,
        "promotors": promotorresults,
        "states": states,
        "cities": cities,
    }
    return render_template("promotors/promotors.html", **context)


@promotor.route("/editpromotor/<id>", methods=["GET", "POST"])
@login_required
def promotoredit(id):
    if request.method == "POST":
        all = request.form.to_dict()
        print(all)
        promotor_edit(id, **all)
        return redirect(url_for("promotor.promotorlist"))
    promotors = db.session.query(Promotors).filter_by(id=id).all()
    states = db.session.query(States).all()
    cities = (
        db.session.query(Promotors.city)
        .distinct(Promotors.city)
        .order_by(Promotors.city)
        .all()
    )
    context = {"user": User, "states": states, "promotors": promotors, "cities": cities}
    return render_template("promotors/promotors_edit.html", **context)


@promotor.route("/deletepromotor/<id>")
@login_required
def promotordelete(id):
    promotor_delete(id)
    return redirect(request.referrer)
