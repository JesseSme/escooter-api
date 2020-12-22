# import json
# from collections import OrderedDict
from extensions import me
from datetime import datetime
from mongoengine import signals


class Temperatures(me.EmbeddedDocument):
    out                 = me.DecimalField(precision=2)
    batt                = me.DecimalField(precision=2)
    fet                 = me.DecimalField(precision=2)
    motor               = me.DecimalField(precision=2)


# TODO: Test Controller -model
class Controller(me.Document):

    location            = me.GeoPointField(required=True)
    temps               = me.EmbeddedDocumentField(Temperatures, default=Temperatures)
    avg_motorcurrent    = me.DecimalField()
    avg_inputcurrent    = me.DecimalField()
    input_voltage       = me.DecimalField()
    rpm                 = me.DecimalField()
    tachometer          = me.DecimalField()
    scooter_time        = me.DateTimeField()
    created_at          = me.DateTimeField()
    updated_at          = me.DateTimeField()


    # https://stackoverflow.com/a/6602255/11426304
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Controller, self).save(*args, **kwargs)


    # Could be needed later on
#    @classmethod
#    def set_validator(self):
#       validator = {}
#       with open('validators\controller.json') as validator_file:
#       validator = json.load(validator_file)
#       od = OrderedDict(validator)
#       me.command(od)
