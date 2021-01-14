from flask import request, Response, session
from flask_restful import Resource
from flask_socketio import send, emit
from flask_googlemaps import Map
from flask import render_template, make_response
from http import HTTPStatus

from extensions import socketio
from secret import GOOGLEMAPS_KEY_SECRET


class HomeResource(Resource):

    def get(self):
        # headers = {"Content-Type": "text/html"}

        return make_response(render_template("index.html", async_mode=socketio.async_mode), 200, )


    def post(self):
        pass