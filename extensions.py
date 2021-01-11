from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_googlemaps import GoogleMaps

me = MongoEngine()
jwt = JWTManager()
maps = GoogleMaps()