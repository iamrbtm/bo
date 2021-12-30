from bo import db
from bo.models import *
from flask_login import current_user


def catagory_add(add_catagory):
    cnt = db.session.query(Eventcat).filter(Eventcat.catagory == add_catagory).count()
    if cnt == 0:
        new = Eventcat(
            catagory = add_catagory.title(),
            userid = current_user.id
        )
        db.session.add(new)
        db.session.commit()
        msg = True
    else:
        msg = "Duplicate Catagory"
    return msg