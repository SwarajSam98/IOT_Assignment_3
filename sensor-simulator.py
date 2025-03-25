import paho.mqtt.client as mqtt
import random
import time
import json

# MQTT Configuration
MQTT_BROKER = "mqtt.eclipseprojects.io"  # Public MQTT broker (replace with AWS IoT if needed)
MQTT_PORT = 1883
MQTT_TOPIC = "iot/environment/{station_id}"  # Dynamic topic based on station ID

# Generate random sensor data
def generate_sensor_data(station_id):
    return {
        "station_id": station_id,
        "temperature": round(random.uniform(-50, 50)),  # °C
        "humidity": round(random.uniform(0, 100)),      # %
        "co2": round(random.uniform(300, 2000)),       # ppm
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }


# MQTT Publisher
def publish_sensor_data(station_id="station_1", interval=5):
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT)

    try:
        while True:
            sensor_data = generate_sensor_data(station_id)
            client.publish(
                MQTT_TOPIC.format(station_id=station_id),
                json.dumps(sensor_data)
            )
            print(f"Published: {sensor_data}")
            time.sleep(interval)
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    publish_sensor_data(station_id="station_1")  # Change ID for multiple stations