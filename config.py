from secret import MONGODB_PASS, JWT_KEY, JWT_ERROR_KEY

class Config:

    MONGO_URI = "mongodb+srv://IAmRoot:{}@iot.fnq30.mongodb.net/tracking?retryWrites=true&w=majority".format(MONGODB_PASS)
    SECRET_KEY = JWT_KEY
    JWT_ERROR_MESSAGE_KEY = JWT_ERROR_KEY