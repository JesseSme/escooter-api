from flask import session, jsonify
from flask_restful import Resource
from flask_socketio import send, emit
import json

from models.controller import Controller, Temperatures

from extensions import socketio, me

class WebSocketResource(Resource):
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
        WebSocketResource.inc_receive()
        scooter_data = Controller.objects.order_by("-updated_at").first()
        scooter_data = scooter_data.to_json()
        scooter_json = json.loads(scooter_data)
        scooter_json.pop("_id")
        emit("response", {"message": json.dumps(scooter_json), "count": session["receive_count"]})


    @socketio.on("power_signal", namespace="/")
    def power_signal_event(message):
        session["receive_count"] = session.get("receive_count", 0) + 1
        #if state == "on":
        #Send turn on to controller
        #Opposite on off
        print(message["state"])
        print(message["pass"])

        emit("response", {"message": "Power signal sent.", "count": session["receive_count"]})