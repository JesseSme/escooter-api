from flask import request
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus
from datetime import datetime

from models.controller import Controller, Temperatures
from models.identifier import Identifiers

class ControllerResource(Resource):

    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        data = request.get_json()

        controllerData = Controller(
            location=data["location"],
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
            scooter_time=datetime.datetime.fromtimestamp(data["epoch"]),
            created_at=datetime.now()
        )

        if Identifiers.objects(identifier=data["identifier"]):
            return HTTPStatus.UNAUTHORIZED

        controllerData.save()

        return data, HTTPStatus.OK

