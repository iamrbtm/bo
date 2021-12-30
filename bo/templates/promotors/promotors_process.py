from bo import db
from bo.models import *
from flask_login import current_user
from flask import flash


def format_tel(phone):
    if phone != "":
        phone = phone.replace("-", "")
        return format(int(phone[:-1]), ",").replace(",", "-") + phone[-1]
    else:
        return ""


def promotor_add(
    fname, lname, company, address, city, state, zip, phone, cell, fax, email
):
    cnt = (
        db.session.query(Promotors)
        .filter(Promotors.fname == fname)
        .filter(Promotors.lname == lname)
        .filter(Promotors.company == company)
        .filter(Promotors.userid == current_user.id)
        .count()
    )

    if cnt == 0:
        fmtphone = format_tel(phone)
        fmtfax = format_tel(fax)
        fmtcell = format_tel(cell)

        new = Promotors(
            fname=fname.title(),
            lname=lname.title(),
            company=company.title(),
            address=address.title(),
            city=city.title(),
            state=state,
            zip=zip,
            phone=fmtphone,
            mobile=fmtcell,
            fax=fmtfax,
            email=email,
            userid=current_user.id,
        )
        db.session.add(new)
        db.session.commit()
    else:
        flash("promotor already exists in the database", catagory="error")


def promotor_delete(id):
    db.session.query(Promotors).filter(Promotors.userid == current_user.id).filter(Promotors.id == id).delete()
    db.session.commit()


def promotor_edit(
    id, fname, lname, company, address, city, state, zip, phone, cell, fax, email
):
    promotor = db.session.query(Promotors).filter(Promotors.userid == current_user.id).filter_by(id=id).first()
    if phone != promotor.phone:
        fmtphone = format_tel(phone)
    else:
        fmtphone = phone

    if fax != promotor.fax:
        fmtfax = format_tel(fax)
    else:
        fmtfax = fax

    if cell != promotor.mobile:
        fmtcell = format_tel(cell)
    else:
        fmtcell = cell

    promotor.fname = fname
    promotor.lname = lname
    promotor.company = company
    promotor.address = address
    promotor.city = city
    promotor.state = state
    promotor.zip = zip
    promotor.phone = fmtphone
    promotor.fax = fmtfax
    promotor.mobile = fmtcell
    promotor.email = email
    promotor.userid = current_user.id
    db.session.commit()
