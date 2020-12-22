from flask import request
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus

from extensions import me

from models.controller import Controller

class ControllerResource(Resource):

    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        data = request.get_json()

        controllerData = Controller(
            identifier=data["identifier"]
        )

        identifier = data['identifier']
        if c.get_by_identifier(identifier) != True:
            return HTTPStatus.UNAUTHORIZED

        me.save(data)
        data.pop("_id")

        return data, HTTPStatus.OK

