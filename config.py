from secret import Secret

class Config:

    MONGODB_URI = "mongodb+srv://IAmRoot:{}@iot.fnq30.mongodb.net/tracking?retryWrites=true&w=majority".format(Secret.MONGODB_PASS)