from flask import request
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus

from models.controller import Controller

class ControllerResource(Resource):

    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        data = request.get_json()

        identifier = data.get('identifier')
        if c.get_by_identifier(identifier) != True:
            return HTTPStatus.UNAUTHORIZED

        save(data)
        data.pop("_id")

        return data, HTTPStatus.OK

