from secret import *

class Config:

    MONGODB_SETTINGS = {
        "db": "tracking",
        "host": "mongodb+srv://IAmRoot:{}@iot.fnq30.mongodb.net/tracking?retryWrites=true&w=majority".format(MONGODB_PASS_SECRET),
        "connectTimeoutMS": 30000,
        "socketTimeoutMS": None,
        "socketKeepAlive": True,
        "connect": False,
        "maxPoolsize": 1
    }
    # MONGO_URI =
    SECRET_KEY = SECRET_KEY_SECRET
    JWT_ERROR_MESSAGE_KEY = JWT_ERROR_KEY_SECRET
    GOOGLEMAPS_KEY = GOOGLEMAPS_KEY_SECRET
    CORS_ALLOW_CREDENTIALS = True
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_HEADERS = "Content-Type"
