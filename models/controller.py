# import json
# from collections import OrderedDict
# from extensions import me
from datetime import datetime
from mongoengine import Document, EmbeddedDocument, DecimalField, EmbeddedDocumentField, DateTimeField, GeoPointField, StringField
from mongoengine import signals


class Temperatures(EmbeddedDocument):
    out                 = DecimalField(precision=2)
    batt                = DecimalField(precision=2)
    fet                 = DecimalField(precision=2)
    motor               = DecimalField(precision=2)


# TODO: Test Controller -model
class Controller(Document):

    location            = GeoPointField(required=True)
    temps               = EmbeddedDocumentField(Temperatures, default=Temperatures)
    avg_motorcurrent    = DecimalField()
    avg_inputcurrent    = DecimalField()
    input_voltage       = DecimalField()
    rpm                 = DecimalField()
    tachometer          = DecimalField()
    scooter_time        = DateTimeField()
    created_at          = DateTimeField()
    updated_at          = DateTimeField()


    # https://stackoverflow.com/a/6602255/11426304
    @classmethod
    def pre_save(cls, sender, document):
        document.updated_at = datetime.now()


    @classmethod
    def get_latest_data(cls):
        return cls.objects.order_by("-updated_at").first()

signals.pre_save.connect(Controller.pre_save, sender=Controller)