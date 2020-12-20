from flask import request
from flask_restful import Resource
import json
from http import HTTPStatus

from models.controllerValidator import controllerValidator

class controllerResource(Resource):


    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        data = request.get_json()

        identifier = data.get('identifier')
        print(data)

        if controllerValidator.get_by_identifier(identifier):
            return HTTPStatus.UNAUTHORIZED

        controllerValidator.save()

        return data, HTTPStatus.OK

"""
class controllerRegisterResource(Resource):

    def post(self):
        data = request.get_json()

        id = data.get('id')
        identifier = data.get('identifier')

        if identifier not cV.get_by_id(identifier):
            return HTTPStatus.UNAUTHORIZED


        return HTTPStatus.OK
"""