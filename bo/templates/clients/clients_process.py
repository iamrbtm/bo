import phonenumbers
from phonenumbers import PhoneNumberFormat
from bo import db
from bo.models import *
from flask_login import current_user
from flask import flash

def format_tel(phone):
    if phone != "":
        phone = phone.replace('-',"")
        return format(int(phone[:-1]), ",").replace(",", "-") + phone[-1]
    else:
        return ""


def client_add(fname, lname, company, address, city, state, zip, phone, cell, fax, email):
    cnt = (
        db.session.query(Clients)
        .filter(Clients.fname == fname)
        .filter(Clients.lname == lname)
        .filter(Clients.company == company)
        .count()
    )

    if cnt == 0:
        fmtphone = format_tel(phone)
        fmtfax = format_tel(fax)
        fmtcell = format_tel(cell)

        new = Clients(
            fname=fname.title(),
            lname=lname.title(),
            company=company.title(),
            address=address.title(),
            city=city.title(),
            state=state,
            zip=zip,
            phone=fmtphone,
            mobile = fmtcell,
            fax=fmtfax,
            email=email,
            userid=current_user.id,
        )
        db.session.add(new)
        db.session.commit()
    else:
        flash("Client already exists in the database", catagory="error")


def client_delete(id):
    db.session.query(Clients).filter(Clients.id == id).delete()
    db.session.commit()

def client_edit(id, fname, lname, company, address, city, state, zip, phone, cell, fax, email):
    client = db.session.query(Clients).filter_by(id=id).first()
    if phone != client.phone:
        fmtphone = format_tel(phone)
    else:
        fmtphone = phone
    
    if fax != client.fax:
        fmtfax = format_tel(fax)
    else:
        fmtfax = fax
    
    if cell != client.mobile:
        fmtcell = format_tel(cell)
    else:
        fmtcell = cell
        
    client.fname = fname
    client.lname = lname
    client.company = company
    client.address = address
    client.city = city
    client.state = state
    client.zip = zip
    client.phone = fmtphone
    client.fax = fmtfax
    client.mobile = fmtcell
    client.email = email
    client.userid = current_user.id
    db.session.commit()
    