from flask import request
from flask_restful import Resource
from flask import jsonify
from http import HTTPStatus

class TestResource(Resource):

    def get(self):
        return {"message": "from TestResource"}