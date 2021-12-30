from bo import db, photos
from bo.models import *
from flask_login import current_user
from flask import flash
import validators
from bo.utilities import format_tel


def venue_add(name, address, city, state, zip, phone, website, loadinst):
    fmtphone = format_tel(phone)
    if validators.url(website):
        website = website
    else:
        website = None
    new = Venue(
        name=name.title(),
        address=address.title(),
        city=city.title(),
        state=state,
        zip=zip,
        phone=fmtphone,
        website=website,
        loadinst=loadinst,
        userid=current_user.id,
    )
    db.session.add(new)
    db.session.commit()


def seating_add(id, type, seating, addseat):
    new = SeatingCompasity(
        seating=seating, seating_type=type, venuefk=id, userid=current_user.id
    )
    db.session.add(new)
    db.session.commit()


def promotor_link(id, promotor, linkpromotor):
    new = Promotor_Venue(promotorfk=promotor, venuefk=id, userid=current_user.id)
    db.session.add(new)
    db.session.commit()
