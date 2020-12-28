# import json
# from collections import OrderedDict
# from extensions import me
from datetime import datetime
from mongoengine import *
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

signals.pre_save.connect(Controller.pre_save, sender=Controller)

    # Could be needed later on
#    @classmethod
#    def set_validator(self):
#       validator = {}
#       with open('validators\controller.json') as validator_file:
#       validator = json.load(validator_file)
#       od = OrderedDict(validator)
#       me.command(od)
