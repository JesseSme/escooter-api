from flask import request, Response
from flask_restful import Resource
from flask import render_template, make_response
from http import HTTPStatus


class LocationResource(Resource):

    # Gets the latest location available from the database.
    # Should this be in the ControllerResource?
    def get(self):
        pass

    def post(self):
        pass