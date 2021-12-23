from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
photos = UploadSet("photos", IMAGES)
uploads = UploadSet("uploads", ALL)

def create_app():
    app = Flask(__name__)

    app.config["UPLOADED_PHOTOS_DEST"] = "bo/static/images"
    app.config["UPLOADED_UPLOADS_DEST"] = "bo/static/uploads"
    configure_uploads(app, photos)
    configure_uploads(app, uploads)
    app._static_folder = "static"

    app.config["SECRET_KEY"] = "helloworld"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

    toolbar = DebugToolbarExtension(app)
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    db.init_app(app)

    Migrate(app, db)

    from bo.templates.base.base import base
    from bo.auth import auth
    from bo.templates.promotors.promotors import promotor
    from bo.templates.venue.venue import venue
    from bo.templates.event.event import events

    app.register_blueprint(base, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(promotor, url_prefix="/promotors")
    app.register_blueprint(venue, url_prefix="/venue")
    app.register_blueprint(events, url_prefix="/events")

    from bo.models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    db.create_all(app=app)
    print("Created database!")
