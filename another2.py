from flask import Flask
from flask import json
from flask import request
import os
import paho.mqtt.client as mqttClient
app = Flask(__name__)

broker_address= str(os.environ["mqtt-host"])
port = int(os.environ["mqtt-port"])
user = str(os.environ["mqtt-user"])
password = str(os.environ["mqtt-pwd"])

client = mqttClient.Client("Python")
client.username_pw_set(user, password=password)
client.connect(broker_address, port=port)

json = []


@app.route('/', methods=['GET'])
def returnAll():
    return request.args.get('hub.challenge')


@app.route('/', methods=['POST'])
def addOne():
    new_json = request.get_json()
    if new_json['entry'][0]['changes'][0]['value']['item'] == 'like':
        client.publish('fb-posts-updates', 'Got like!')
        client.disconnect()
        return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",5000)))

