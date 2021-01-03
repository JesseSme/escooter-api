from secret import MONGODB_PASS, JWT_KEY, JWT_ERROR_KEY

class Config:

    MONGODB_SETTINGS = {
        "db": "tracking",
        "host": "mongodb+srv://IAmRoot:{}@iot.fnq30.mongodb.net/tracking?retryWrites=true&w=majority".format(MONGODB_PASS),
        "connectTimeoutMS": 30000,
        "socketTimeoutMS": None,
        "socketKeepAlive": True,
        "connect": False,
        "maxPoolsize": 1
    }
    # MONGO_URI =
    SECRET_KEY = JWT_KEY
    JWT_ERROR_MESSAGE_KEY = JWT_ERROR_KEY