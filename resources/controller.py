from flask import request
from flask_restful import Resource
import json
from http import HTTPStatus

class controllerResource(Resource):


    # Handles incoming controller data.
    # TODO: Add sender validation. Tokens, users etc.
    def post(self):
        data = request.data
        json_object = json.loads(data)
        json_formatted = json.dumps(json_object, indent=2)

        print(json_formatted)

        return HTTPStatus.CREATED