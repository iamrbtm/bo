from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime
from sqlalchemy.orm import backref, relationship
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
    avatar_url = db.Column(db.String(250))
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
    #relationship
    promotor_venue = db.relationship("Promotor_Venue", backref='prom')


class Promotor_Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promotorfk = db.Column(db.Integer, db.ForeignKey("promotors.id", ondelete='CASCADE'))
    venuefk = db.Column(db.Integer, db.ForeignKey("venue.id", ondelete='CASCADE'))
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
    #relationship
    promotor_venue = db.relationship("Promotor_Venue", backref='venue')


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
    event_artistfk = db.Column(db.Integer, db.ForeignKey("artist.id"))
    event_tourfk = db.Column(db.Integer, db.ForeignKey("tour.id"))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Eventcat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tourname = db.Column(db.String(150))
    headliner1 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    headliner2 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    headliner3 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    opener1 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    opener2 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    opener3 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    opener4 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    opener5 = db.Column(db.Integer, db.ForeignKey("artist.id"))
    tour_banner_filename = db.Column(db.String(100))
    tour_banner_url = db.Column(db.String(200))
    tour_banner_note = db.Column(db.Text)
    tour_artwork1_filename = db.Column(db.String(100))
    tour_artwork1_url = db.Column(db.String(200))
    tour_artwork1_note = db.Column(db.Text)
    tour_artwork2_filename = db.Column(db.String(100))
    tour_artwork2_url = db.Column(db.String(200))
    tour_artwork2_note = db.Column(db.Text)
    tour_artwork3_filename = db.Column(db.String(100))
    tour_artwork3_url = db.Column(db.String(200))
    tour_artwork3_note = db.Column(db.Text)
    tour_artwork4_filename = db.Column(db.String(100))
    tour_artwork4_url = db.Column(db.String(200))
    tour_artwork4_note = db.Column(db.Text)
    tour_artwork5_filename = db.Column(db.String(100))
    tour_artwork5_url = db.Column(db.String(200))
    tour_artwork5_note = db.Column(db.Text)
    userid = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Artistcat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(100))
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100))
    artist_band = db.Column(db.Boolean)
    artist_solo = db.Column(db.Boolean)
    artist_banner_filename = db.Column(db.String(100))
    artist_banner_url = db.Column(db.String(200))
    artist_artwork1_filename = db.Column(db.String(100))
    artist_artwork1_url = db.Column(db.String(200))
    artist_artwork1_note = db.Column(db.Text)
    artist_artwork2_filename = db.Column(db.String(100))
    artist_artwork2_url = db.Column(db.String(200))
    artist_artwork2_note = db.Column(db.Text)
    artist_artwork3_filename = db.Column(db.String(100))
    artist_artwork3_url = db.Column(db.String(200))
    artist_artwork3_note = db.Column(db.Text)
    artist_artwork4_filename = db.Column(db.String(100))
    artist_artwork4_url = db.Column(db.String(200))
    artist_artwork4_note = db.Column(db.Text)
    artist_artwork5_filename = db.Column(db.String(100))
    artist_artwork5_url = db.Column(db.String(200))
    artist_artwork5_note = db.Column(db.Text)
    userid = db.Column(db.Integer)
    update_time = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # forign key
    artist_catagoryfk = db.Column(db.Integer, db.ForeignKey("artistcat.id"))


# class <name>(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     userid = db.Column(db.Integer)
#     update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     date_created = db.Column(db.DateTime(timezone=True), default=func.now())
