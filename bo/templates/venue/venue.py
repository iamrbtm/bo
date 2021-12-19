from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from bo.models import *
from bo.templates.venue.venue_process import *
from bo.templates.people.people_process import *


venue = Blueprint("venue", __name__)

@venue.route("/", methods=['GET','POST'])
def venuelist():
    if request.method == "POST":
        all = request.form.to_dict()
        print(all)
        venue_add(**all)
        
    venues = db.session.query(Venue).all()
    states = db.session.query(States).all()
    cities = db.session.query(Venue.city).distinct(Venue.city).order_by(Venue.city).all()
    context = {'user':User, 'venues':venues, 'states':states, 'cities':cities}
    return render_template('venue/venue.html', **context)

@venue.route('venuedelete/<id>', methods=['GET','POST'])
def venuedelete(id):
    db.session.query(People).filter_by(venuefk=id).delete()
    db.session.query(SeatingCompasity).filter_by(venuefk=id).delete()
    db.session.query(Venue).filter_by(id=id).delete()
    db.session.commit()
    return redirect ('venue.venuesingle', id=id)

@venue.route('venueedit/<id>', methods=['GET','POST'])
def venueedit(id):
    pass

@venue.route('venuesingle/<id>', methods=['GET','POST'])
def venuesingle(id):
    if request.method == "POST":
        all = request.form.to_dict()
        print(all)
        if 'addpeople' in all:
            people_add(id, **all)
        
        if 'addseat' in all:
            seating_add(id, **all)

    
    states = db.session.query(States).all()
    venues = db.session.query(Venue).filter_by(id=id).all()
    peoples = db.session.query(People).filter(People.venuefk == id).all()
    roles = db.session.query(People.role).distinct(People.role).order_by(People.role).all()
    seats = db.session.query(SeatingCompasity).filter_by(venuefk = id).all()
    context ={'user':User, 'states':states, 'venues':venues, 
              'peoples':peoples, 'roles':roles, 'seats':seats}
    return render_template('venue/venue_single.html', **context)