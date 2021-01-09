from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

me = MongoEngine()
jwt = JWTManager()
socketio = SocketIO()
