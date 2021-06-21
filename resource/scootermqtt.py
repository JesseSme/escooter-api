from flask.json import jsonify
from flask_mongoengine import json
from extensions import mqtt, scooterData

from models.identifier import Identifier
from models.controller import Controller, Temperatures

from datetime import datetime

@mqtt.on_topic("arduino/outgoing")
def handle_arduino_outgoing(client, userdata, message):
    print('Received message on topic {}: {}'
          .format(message.topic, message.payload.decode()))

@mqtt.on_topic("arduino/incoming")
def handle_arduino_incoming(client, userdata, message):
    print('Received message on topic {}: {}'
          .format(message.topic, message.payload.decode()))

@mqtt.on_topic("scooter/jesse/data")
def handle_arduino_outgoing(client, userdata, message):
    data = message.payload.decode()
    print(data)
    data = jsonify(data)
    if not data:
        print("Not registering as json!")
        return
    location = data["location"]
    controllerData = Controller(
        location= [location["longitude"],location["latitude"]],
        temps=Temperatures(
            out=data["temp_out"],
            batt=data["temp_batt"],
            fet=data["temp_fet"],
            motor=data["temp_motor"]
            ),
        avg_motorcurrent=data["average_motorcurrent"],
        avg_inputcurrent=data["average_inputcurrent"],
        input_voltage=data["input_voltage"],
        rpm=data["rpm"],
        tachometer=data["tachometer"],
        scooter_time=datetime.fromtimestamp(data["epoch"]),
        created_at=datetime.now()
    )
    idd = data["identifier"]
    Identifier.objects.get_or_404(identifier=idd)
    try:
        controllerData.save()
    except:
        print({"error": "Something went wrong"})
        return
    print({"message": "Data saved"})
    return

@mqtt.on_topic("scooter/jesse/power")
def handle_scooter_power(client, userdata, message):
    data = message.payload.decode()
    print(data)