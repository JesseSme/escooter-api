from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

me = MongoEngine()
jwt = JWTManager()