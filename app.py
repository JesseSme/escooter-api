from flask import Flask
from flask_restful import Api
from resources import database


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):


def register_resources(app):
    api = Api(app)
    api.add_resource(databaseResource, "/api/db")


if __name__ == "__main__":
    app.run()
