# Flask modules
from flask import Flask, render_template, url_for
from flask_restful import Api

# Resources
from resource.controller import ControllerResource, ControllerPowerResource
from resource.home import HomeResource
from resource.socket import WebSocketResource

# Settings and extensions
from config import Config
from extensions import jwt, maps, me, socketio, apsheduler # cors


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
    socketio.init_app(app)
    apsheduler.init_app(app)



def register_resources(app):
    api = Api(app)
    api.add_resource(ControllerResource, '/ipa/controller')
    api.add_resource(ControllerPowerResource, "/ipa/power_state")
    api.add_resource(HomeResource, "/")


app = create_app()

if __name__ == "__main__":
    app.run()
