from flask import request, make_response
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus
from datetime import datetime
import time

import json

from models.controller import Controller, Temperatures
from models.identifier import Identifier

from utilities import verify_password, hash_password
from extensions import mqtt, scooterData

from secret import POWER_PASSWORD



class ControllerResource(Resource):

    def get(self):
        scooter_data = Controller.get_latest_data()
        scooter_data = scooter_data.to_json()
        scooter_json = json.loads(scooter_data)
        scooter_json.pop("_id")
        return make_response(scooter_json, 200)

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

    timeSinceSwitch = 0

    def get(self):
        return getattr(scooterData, "power_state"), HTTPStatus.OK

    def post(self):
        if not request.is_json:
            return {"error": "unsupported media."}, HTTPStatus.UNSUPPORTED_MEDIA_TYPE
        message = request.get_json(force=True)
        print(message)
        outmessage = ""
        state = ""

        # TODO: Make this if-else clearer
        if time.time() - ControllerPowerResource.timeSinceSwitch > 15:
            if verify_password(message["pass"], hash_password(POWER_PASSWORD)):
                if message["state"] == "Turn on":
                    if scooterData.power_state == 0:
                        setattr(scooterData, "power_state", 1)
                    outmessage = "On signal sent."
                    state = "Turn off"
                    ControllerPowerResource.timeSinceSwitch = time.time()
                elif message["state"] == "Turn off":
                    if scooterData.power_state == 1:
                        setattr(scooterData, "power_state", 0)
                    outmessage = "Off signal sent."
                    state = "Turn on"
                    ControllerPowerResource.timeSinceSwitch = time.time()
                else:
                    message = -1
            else:
                message = -1
        else:
            message = -1
            outmessage = "tryagain soon in: {}".format(15 - (time.time() - ControllerPowerResource.timeSinceSwitch))
        if not message == -1:
            mqtt.publish("scooter/jesse/power", scooterData.power_state)
        return make_response({"state": state, "message": outmessage}, 200)