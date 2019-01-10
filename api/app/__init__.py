from flask import Flask

from app import configuration
from app.routes.apiv1 import api_v1
from app.routes.default_api import default_api

from app.extensions import db
from app.extensions import ma
from app.extensions import cors


def create_app(config=configuration.BaseConfig):
    application = Flask(__name__)
    application.config.from_object(config)

    register_blueprint(application)
    register_extensions(application)
    return application


def register_blueprint(application):
    application.register_blueprint(api_v1)
    application.register_blueprint(default_api)


def register_extensions(application):
    db.init_app(application)
    ma.init_app(application)
    cors.init_app(application)
