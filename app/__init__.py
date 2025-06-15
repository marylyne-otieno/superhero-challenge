
# app/__init__.py
from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    from app.routes import api
    app.register_blueprint(api)

    return app
