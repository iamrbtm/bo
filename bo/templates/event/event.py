from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from flask_login.utils import login_required
from bo.models import *
from bo.templates.event.event_process import *


events = Blueprint("events", __name__)


@events.route("/", methods=["GET", "POST"])
@login_required
def eventlist():
    
    context = {'user':User}
    return render_template('event/event.html', **context)