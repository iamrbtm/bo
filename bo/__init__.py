from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import env
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL



db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)
uploads = UploadSet('uploads', ALL)

def create_app():
    app = Flask(__name__)
    
    app.config['UPLOADED_PHOTOS_DEST'] = 'bo/static/images'
    app.config['UPLOADED_UPLOADS_DEST'] = 'bo/static/uploads'
    configure_uploads(app, photos)
    configure_uploads(app, uploads)
    app._static_folder = 'static'
    
    app.config["SECRET_KEY"] = "helloworld"
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{env.DB_USERNAME}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}"

    DebugToolbarExtension(app)
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    db.init_app(app)
    
    Migrate(app, db)

    from bo.views import views
    from bo.auth import auth
    from bo.templates.clients.clients import client
    from bo.templates.venue.venue import venue

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(client, url_prefix="/clients")
    app.register_blueprint(venue, url_prefix="/venue")


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
