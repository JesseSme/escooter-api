from flask import Flask
from flask_restful import Api
from resources.controller import controllerResource
from models.controllerValidator import controllerValidator

from config import Config
from extensions import mongo, jwt

import json


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    mongo.init_app(app)
    controllerValidator.set_validator()
    jwt.init_app(app)


def register_resources(app):
    api = Api(app)
    api.add_resource(controllerResource, '/api/db')



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
