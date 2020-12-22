from flask import Flask
from flask_restful import Api
from resources.controller import ControllerResource
from models.controller import Controller

from config import Config
from extensions import jwt

import mongoengine


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db = mongoengine
    db.connect()
    print(db.connection)
    jwt.init_app(app)


def register_resources(app):
    api = Api(app)
    api.add_resource(ControllerResource, '/api/db')



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
