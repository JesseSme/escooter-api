from extensions import me

class Identifiers(me.Document):
    identifier              = me.StringField(required=True)

    @classmethod
    def get_by_identifier(cls, identifier):
        return cls._get_collection