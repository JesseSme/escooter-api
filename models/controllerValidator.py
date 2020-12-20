from extensions import mongo

class controllerValidator():

    @classmethod
    def get_by_identifier(self, identifier):
        return mongo.db.identifications.find_one({"identifier": identifier})


    def save(self, data):
        mongo.db.scooter.save(data)
