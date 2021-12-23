from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from flask_login.utils import login_required
import sqlalchemy
from bo.models import *
from bo.templates.event.event_process import *


events = Blueprint("events", __name__)


@events.route("/", methods=["GET", "POST"])
@login_required
def eventlist():
    
    promotors = db.session.query(Promotors).all()
    venues = db.session.query(Venue).all()
    allevents = db.session.query(Events).filter(sqlalchemy.extract('year', Events.event_start_datetime) == 2022).order_by(Events.event_start_datetime).all()
    eventcat = db.session.query(Eventcat).all()
    context = {'user':User, 'promotors':promotors,
               'venues':venues, 'allevents':allevents,
               'eventcat':eventcat}
    return render_template('event/event.html', **context)