from flask import request, make_response
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus
from datetime import datetime
# from extensions import me
from models.controller import Controller, Temperatures
from models.identifier import Identifier

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
        self.remember_scooter_ip(self, idd, data["sender_ip"])

        return {"message": "Data saved"}, HTTPStatus.OK

    @staticmethod
    def remember_scooter_ip(self, identifier, ip):
        global identity
        if not identity:
            if identifier not in identity:
                identity[identifier] = ip


class ControllerPowerResource(Resource):
