from flask import Flask
from flask import jsonify
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
        mqttc = mqttClient.Client()
        mqttc.username_pw_set(os.environ.get("mqtt-user", ''), os.environ.get("mqtt-pwd", ''))
        mqttc.connect(os.environ.get("mqtt-host", ''), int(os.environ.get("mqtt-port", 	5001)))
        mqttc.publish('fb-posts-updates', 'Got like!')
        mqttc.disconnect()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",5000)))

