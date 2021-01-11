from flask import Flask, render_template
from flask_restful import Api

from resource.controller import ControllerResource
from resource.test import TestResource

from models.controller import Controller

from config import Config
from extensions import jwt, maps, me


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    app.app_context().push()

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    me.init_app(app)
    jwt.init_app(app)
    maps.init_app(app)


def register_resources(app):
    api = Api(app)
    api.add_resource(ControllerResource, '/ipa/controller')
    api.add_resource(TestResource, "/")

app = create_app()


if __name__ == "__main__":
    app.run()
