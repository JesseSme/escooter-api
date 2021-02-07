from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_googlemaps import GoogleMaps
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler

me = MongoEngine()
jwt = JWTManager()
maps = GoogleMaps()
socketio = SocketIO(cors_allowed_origins="*")
apsheduler = APScheduler()
