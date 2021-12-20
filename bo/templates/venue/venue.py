from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from flask_login.utils import login_required
from bo.models import *
from bo.templates.venue.venue_process import *
from bo.templates.people.people_process import *


venue = Blueprint("venue", __name__)


@venue.route("/", methods=["GET", "POST"])
@login_required
def venuelist():
    if request.method == "POST":
        all = request.form.to_dict()
        print(all)
        venue_add(**all)

    venues = db.session.query(Venue).all()
    states = db.session.query(States).all()
    cities = (
        db.session.query(Venue.city).distinct(Venue.city).order_by(Venue.city).all()
    )
    context = {"user": User, "venues": venues, "states": states, "cities": cities}
    return render_template("venue/venue.html", **context)


@venue.route("venuedelete/<id>", methods=["GET", "POST"])
@login_required
def venuedelete(id):
    db.session.query(People).filter_by(venuefk=id).delete()
    db.session.query(SeatingCompasity).filter_by(venuefk=id).delete()
    db.session.query(Venue).filter_by(id=id).delete()
    db.session.commit()
    return redirect("venue.venuesingle", id=id)


@venue.route("venueedit/<id>", methods=["GET", "POST"])
@login_required
def venueedit(id):
    pass


@venue.route("venuesingle/<id>", methods=["GET", "POST"])
@login_required
def venuesingle(id):
    if request.method == "POST":
        all = request.form.to_dict()
        print(all)
        if "addpeople" in all:
            people_add(id, **all)
        elif "addseat" in all:
            seating_add(id, **all)
        elif "linkpromotor" in all:
            promotor_link(id, **all)

    promotors = (
        db.session.query(Promotors)
        .join(Promotor_Venue, Promotor_Venue.promotorfk == Promotors.id)
        .filter(Promotor_Venue.venuefk == id)
        .all()
    )
    states = db.session.query(States).all()
    venues = db.session.query(Venue).filter_by(id=id).all()
    peoples = db.session.query(People).filter(People.venuefk == id).all()
    allpromotors = db.session.query(Promotors).all()
    roles = (
        db.session.query(People.role).distinct(People.role).order_by(People.role).all()
    )
    seats = db.session.query(SeatingCompasity).filter_by(venuefk=id).all()
    peoplelastupdate = (
        db.session.query(func.max(People.update_time).label("updatemax"))
        .filter(People.venuefk == id)
        .scalar()
    )
    seatinglastupdate = (
        db.session.query(func.max(SeatingCompasity.update_time).label("updatemax"))
        .filter(People.venuefk == id)
        .scalar()
    )
    promotorlastupdate = (
        db.session.query(func.max(Promotor_Venue.update_time).label("updatemax"))
        .filter(Promotor_Venue.venuefk == id)
        .scalar()
    )

    context = {
        "user": User,
        "states": states,
        "venues": venues,
        "peoples": peoples,
        "roles": roles,
        "seats": seats,
        "promotors": promotors,
        "allpromotors": allpromotors,
        "peoplelastupdate": peoplelastupdate,
        "seatinglastupdate": seatinglastupdate,
        "promotorlastupdate": promotorlastupdate,
    }
    return render_template("venue/venue_single.html", **context)
