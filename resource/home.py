from flask import request, Response, session
from flask_restful import Resource
from flask_socketio import socketio
from flask import render_template, make_response
from http import HTTPStatus


class HomeResource(Resource):

    def get(self):
        # headers = {"Content-Type": "text/html"}

        return make_response(render_template("index.html"), HTTPStatus.OK, )


    def post(self):
        pass