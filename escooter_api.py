# Flask modules
from flask import Flask, render_template, url_for
from flask_restful import Api

# Resources
from resource.controller import ControllerResource, ControllerPowerResource
from resource.home import HomeResource
from resource.socket import WebSocketResource

# Settings and extensions
from config import Config
import ssl
from extensions import jwt, maps, me, socketio, apsheduler, cors, mqtt


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    app.config['MQTT_TLS_CERT_REQS'] = ssl.CERT_REQUIRED
    app.config['MQTT_TLS_VERSION'] = ssl.PROTOCOL_TLSv1_2
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
    cors.init_app(app)
    mqtt.init_app(app)



def register_resources(app):
    api = Api(app)
    api.add_resource(ControllerResource, '/ipa/controller')
    api.add_resource(ControllerPowerResource, "/ipa/power_state")
    api.add_resource(HomeResource, "/")


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("Connected and waiting for messages")
    mqtt.subscribe("arduino/#")
    mqtt.subscribe("scooter/#")

import resource.scootermqtt


app = create_app()

if __name__ == "__main__":
    app.run()
