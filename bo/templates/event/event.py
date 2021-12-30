from flask import Blueprint, render_template, redirect, request, flash
from flask.helpers import url_for
from flask_login.utils import login_required
import sqlalchemy
from datetime import date
from bo.models import *
from bo.templates.event.event_process import *


events = Blueprint("events", __name__)


@events.route("/", methods=["GET", "POST"])
@login_required
def eventlist():
    
    promotors = db.session.query(Promotors).all()
    venues = db.session.query(Venue).all()
    allevents = db.session.query(Events).filter(func.Date(Events.event_start_datetime) >= date.today()).order_by(Events.event_start_datetime).limit(50)
    eventcat = db.session.query(Eventcat).all()
    context = {'user':User, 'promotors':promotors,
               'venues':venues, 'allevents':allevents,
               'eventcat':eventcat}
    return render_template('event/event.html', **context)

@events.route("/add", methods=["GET", "POST"])
@login_required
def eventadd():
    if request.method == "POST":
        all = request.form.to_dict()
        msg = catagory_add(**all)
        if not msg == True:
            flash(msg, category="error")
    catagories = db.session.query(Eventcat).filter(Eventcat.userid == current_user.id).all()
    venues = db.session.query(Venue).filter(Venue.userid == current_user.id).all()
    promotors = db.session.query(Promotors).filter(Promotors.userid == current_user.id).all()

    context = {'user':User, 'catagories':catagories, 'venues':venues, 'promotors':promotors}
    return render_template('event/event_add.html', **context)