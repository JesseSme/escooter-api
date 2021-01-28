from flask import request, Response
from flask_restful import Resource
from flask import render_template, make_response
from http import HTTPStatus



class TestResource(Resource):

    def get(self):

        return make_response("<div>Im in test</div>", 200)

class TestTwoResource(Resource):
    def get(self):
        return make_response("<div>Im in test 2</div>", 200)