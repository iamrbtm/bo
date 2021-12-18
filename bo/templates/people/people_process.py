from bo import db
from bo.models import *
from flask_login import current_user
from flask import flash
import validators


def format_tel(phone):
    if phone != "":
        phone = phone.replace("-", "")
        return format(int(phone[:-1]), ",").replace(",", "-") + phone[-1]
    else:
        return ""


def people_add(id, fname, lname, role, phone, email, addpeople):
    if not validators.email(email):
        email = ""
    new = People(
        venuefk=id,
        fname=fname.title(),
        lname=lname.title(),
        role=role.title(),
        phone=format_tel(phone),
        email=email,
        userid=current_user.id,
    )
    db.session.add(new)
    db.session.commit()
