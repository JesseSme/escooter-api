from flask import request
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus

from models.controllerValidator import controller

class controllerResource(Resource):

    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        c = controller()
        data = request.get_json()

        identifier = data.get('identifier')

        if c.get_by_identifier(identifier) != True:
            return HTTPStatus.UNAUTHORIZED

        c.save(data)
        data.pop("_id")

        return data, HTTPStatus.OK

