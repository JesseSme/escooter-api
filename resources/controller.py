from flask import request
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus

from models.controllerValidator import controllerValidator

class controllerResource(Resource):

    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        cV = controllerValidator()
        data = request.get_json()

        identifier = data.get('identifier')

        if cV.get_by_identifier(identifier) != True:
            return HTTPStatus.UNAUTHORIZED

        cV.save(data)
        data.pop("_id")

        return data, HTTPStatus.OK

