from flask import session, jsonify
from flask_restful import Resource
from flask_socketio import send, emit
import json
import requests

from models.controller import Controller, Temperatures
from resource.controller import ControllerPowerResource

from extensions import socketio, me, apsheduler
from secret import POWER_PASSWORD
from utilities import hash_password, verify_password

power_password = POWER_PASSWORD

class WebSocketResource(Resource):

    location = [60.4353, 22.2287]   # Initial coordinates, when the program starts.
    scooter_data = 0


    def __init__(self):
        pass


    @staticmethod
    def inc_receive():
        session["receive_count"] = session.get("receive_count", 0) + 1


    @socketio.on("hello", namespace="/")
    def hello_event(message):
        WebSocketResource.inc_receive()
        emit("response", {"message": message["data"] , "count": session["receive_count"]})


    @socketio.on("scooter_info", namespace="/")
    def scooter_info_event(message):
        scooter_data = Controller.get_latest_data()
        scooter_data = scooter_data.to_json()
        scooter_json = json.loads(scooter_data)
        scooter_json.pop("_id")
        emit("dataresponse", {"message": json.dumps(scooter_json), "count": session["receive_count"]})


    @socketio.on("geoloc", namespace="/")
    def geoloc_event(self):
        emit("georesp", {"latitude": WebSocketResource.location[0], "longitude": WebSocketResource.location[1]})
        WebSocketResource.location[0] = WebSocketResource.location[0] + 1
        print(WebSocketResource.location[0])


    @socketio.on("power_signal", namespace="/")
    def power_signal_event(message):
        outmessage = ""
        state = ""
        WebSocketResource.inc_receive()
        if verify_password(message["pass"], hash_password(POWER_PASSWORD)):
            if message["state"] == "Turn on":
                ControllerPowerResource.power_state = 1
                outmessage = "On signal sent."
                state = "Turn off"
            elif message["state"] == "Turn off":
                ControllerPowerResource.power_state = 0
                outmessage = "Off signal sent."
                state = "Turn on"
            else:
                message = "Something went wrong"
        else:
            message = "Wrong password."
        emit("power_response", {"state": state, "message": outmessage, "count": session["receive_count"]})
