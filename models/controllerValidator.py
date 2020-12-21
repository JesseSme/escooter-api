from extensions import mongo
import json
from collections import OrderedDict
from flask import jsonify

class controllerValidator():

    @classmethod
    def set_validator(self):
        validator = {}
        with open('validators\controllerValidator.json') as validator_file:
            validator = json.load(validator_file)
        od = OrderedDict(validator)
        mongo.db.command(od)

    def get_by_identifier(self, identifier):
        print(identifier)
        #mongo.db.identifications.create_index({identifier: "text"})
        gotid = mongo.db.identifications.find_one({"$text": {"$search": "\"{}\"".format(identifier)}})
        if gotid["identifier"] == identifier:
            return True
        return False


    def save(self, data):
        mongo.db.scooter.save(data)
