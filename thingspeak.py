import paho.mqtt.client as mqtt
import json
import requests
from datetime import datetime, timedelta

# === ThingSpeak Channel Config ===
THINGSPEAK_API_KEY = "QUGTM0K2YJY3E033"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def send_to_thingspeak(temperature, humidity, co2):
    try:
        response = requests.get(
            THINGSPEAK_URL,
            params={
                "api_key": THINGSPEAK_API_KEY,
                "field1": temperature,
                "field2": humidity,
                "field3": co2
            },
            timeout=5
        )
        print(f"✅ Sent to ThingSpeak: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error sending to ThingSpeak: {e}")
        return False

def on_connect(client, userdata, flags, rc):
    print("🔌 Connected to MQTT Broker")
    client.subscribe("iot/environment/#")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📥 MQTT Message: {payload}")
        if all(k in payload for k in ['temperature', 'humidity', 'co2']):
            send_to_thingspeak(
                payload["temperature"],
                payload["humidity"],
                payload["co2"]
            )
    except Exception as e:
        print(f"❌ Error handling message: {e}")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("mqtt.eclipseprojects.io", 1883, 60)
        client.loop_forever()
    except Exception as e:
        print(f"❌ MQTT Connection Failed: {e}")
