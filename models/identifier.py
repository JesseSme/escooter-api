from datetime import datetime
from extensions import me

from mongoengine import StringField, DateTimeField
from mongoengine import signals


class Identifier(me.Document):
    identifier              = StringField(required=True, nullable=False, unique=True)
    # password                = StringField(min_length=8, max_length=100, required=True, nullable=False)
    created_at              = DateTimeField(required=True, default=datetime.now)
    updated_at              = DateTimeField(required=True, default=datetime.now)


    @classmethod
    def pre_save(cls, sender, document):
        document.updated_at = datetime.now()


    @classmethod
    def get_by_identifier(cls, identifier):
        return cls.objects.get(identifier=identifier).first()


signals.pre_save.connect(Identifier.pre_save, sender=Identifier)