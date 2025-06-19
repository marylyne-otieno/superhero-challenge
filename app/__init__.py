
from flask import Flask
from app.extensions import db, migrate
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from .resources import register_resources

    api = Api(app)
    register_resources(api)

    return app
