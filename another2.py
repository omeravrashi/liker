from flask import Flask
from flask import jsonify
from flask import request
import os
import paho.mqtt.client as mqttClient
app = Flask(__name__)

broker_address= "m12.cloudmqtt.com"
port = 15881
user = "baaagjli"
password = "qAriS-uGhGQ4"
client = mqttClient.Client("Python")
client.username_pw_set(user, password=password)
client.connect(broker_address, port=port)

json = []

@app.route('/', methods=['GET'])
def returnAll():
    return jsonify({'json': json})


@app.route('/', methods=['POST'])
def addOne():
    new_json = request.get_json()
    json.append(new_json)
    client.publish("python/test",str(new_json))
    return jsonify({'json': json})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",5000)))

