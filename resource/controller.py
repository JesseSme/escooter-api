from flask import request, make_response
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus
from datetime import datetime
# from extensions import me
from models.controller import Controller, Temperatures
from models.identifier import Identifier

from utilities import verify_password, hash_password

from secret import POWER_PASSWORD

identity = {}

class ControllerResource(Resource):

    # Handles incoming controller data.
    # TODO: Add token verification. No high prio.
    def post(self):
        if not request.json:
            return {"error": "unsupported media."}, HTTPStatus.UNSUPPORTED_MEDIA_TYPE
        data = request.get_json()
        print(data)
        location = data["location"]
        controllerData = Controller(
            location= [location["longitude"],location["latitude"]],
            temps=Temperatures(
                out=data["temp_out"],
                batt=data["temp_batt"],
                fet=data["temp_fet"],
                motor=data["temp_motor"]
                ),
            avg_motorcurrent=data["average_motorcurrent"],
            avg_inputcurrent=data["average_inputcurrent"],
            input_voltage=data["input_voltage"],
            rpm=data["rpm"],
            tachometer=data["tachometer"],
            scooter_time=datetime.fromtimestamp(data["epoch"]),
            created_at=datetime.now()
        )
        idd = data["identifier"]
        Identifier.objects.get_or_404(identifier=idd)
        try:
            controllerData.save()
        except:
            return {"error": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR

        return {"message": "Data saved"}, HTTPStatus.OK


class ControllerPowerResource(Resource):

    power_state = 0

    def get(self):
        return ControllerPowerResource.power_state, HTTPStatus.OK

    def post(self):
        if not request.is_json:
            return {"error": "unsupported media."}, HTTPStatus.UNSUPPORTED_MEDIA_TYPE
        message = request.get_json(force=True)
        print(message)
        outmessage = ""
        state = ""
        # WebSocketResource.inc_receive()
        if verify_password(message["pass"], hash_password(POWER_PASSWORD)):
            if message["state"] == "Turn on":
                if ControllerPowerResource.power_state != 1:
                    ControllerPowerResource.power_state = 1
                outmessage = "On signal sent."
                state = "Turn off"
            elif message["state"] == "Turn off":
                if ControllerPowerResource.power_state != 0:
                    ControllerPowerResource.power_state = 0
                outmessage = "Off signal sent."
                state = "Turn on"
            else:
                message = "Something went wrong"
        else:
            message = "Wrong password."
        # emit("power_response", {"state": state, "message": outmessage, "count": session["receive_count"]})
        return {"state": state, "message": outmessage}, HTTPStatus.OK