from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime
from sqlalchemy import ForeignKey


# Users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    address = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(150), unique=True)
    dob = db.Column(db.Date)
    avatar_filename = db.Column(db.Text)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class States(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50))
    abr = db.Column(db.String(2))


class Promotors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    company = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Integer, ForeignKey("states.id"))
    zip = db.Column(db.Text)
    phone = db.Column(db.Text)
    mobile = db.Column(db.Text)
    fax = db.Column(db.Text, default="000-000-0000")
    email = db.Column(db.String(300), unique=True)
    logo = db.Column(db.Unicode(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Promotor_Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promotorfk = db.Column(db.Integer)
    venuefk = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.Integer)
    zip = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    website = db.Column(db.String(100))
    loadinst = db.Column(db.Text)
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class SeatingCompasity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seating = db.Column(db.Integer)
    seating_type = db.Column(db.String(30))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # forign keys
    venuefk = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # forign key
    promotorfk = db.Column(db.Integer, db.ForeignKey("promotors.id"))
    venuefk = db.Column(db.Integer, db.ForeignKey("venue.id"))


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(100))
    event_start_datetime = db.Column(db.DateTime)
    event_end_datetime = db.Column(db.DateTime)
    event_onsale_datetime = db.Column(db.DateTime)
    # forign keys
    event_catagoryfk = db.Column(db.Integer, db.ForeignKey("eventcat.id"))
    event_venuefk = db.Column(db.Integer, db.ForeignKey("venue.id"))
    event_promotorfk = db.Column(db.Integer, db.ForeignKey("promotors.id"))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
   
    
class Eventcat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Artistcat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100))
    artist_band = db.Column(db.Boolean)
    artist_solo = db.Column(db.Boolean)
    artist_picture_filename = db.Column(db.String(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    #forign key
    artist_catagoryfk = db.Column(db.Integer, db.ForeignKey("artistcat.id"))
    
# class <name>(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     userid = db.Column(db.Integer)
#     update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     date_created = db.Column(db.DateTime(timezone=True), default=func.now())
