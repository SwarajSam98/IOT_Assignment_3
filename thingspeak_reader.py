import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# === ThingSpeak Config ===
CHANNEL_ID = "2889169"
READ_API_KEY = "M0FJOW2GWYDFQWU3"

BASE_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
LAST_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json"

def display_latest_data():
    response = requests.get(LAST_URL, params={"api_key": READ_API_KEY})
    data = response.json()
    print("\n🟢 Latest Data from ThingSpeak:")
    print(f"  Time:        {data['created_at']}")
    print(f"  Temperature: {data['field1']} °C")
    print(f"  Humidity:    {data['field2']} %")
    print(f"  CO₂:         {data['field3']} ppm")

def display_historical(field_key):
    response = requests.get(BASE_URL, params={"api_key": READ_API_KEY, "results": 1000})
    feeds = response.json()["feeds"]

    now = datetime.utcnow()
    five_hours_ago = now - timedelta(hours=5)

    timestamps, values = [], []

    for entry in feeds:
        created = datetime.strptime(entry["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if created >= five_hours_ago:
            value = entry.get(field_key)
            if value:
                timestamps.append(created)
                values.append(float(value))

    for t, v in zip(timestamps, values):
        print(f"{t} - {v}")

    # Optional: plot
    plt.plot(timestamps, values, marker="o")
    plt.title(f"{field_key.upper()} over last 5 hours")
    plt.xlabel("Time")
    plt.ylabel(field_key.upper())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

def menu():
    while True:
        print("\n=== ThingSpeak Data Viewer ===")
        print("1. Show latest sensor data")
        print("2. Show last 5 hours for a sensor")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            display_latest_data()
        elif choice == "2":
            sensor = input("Sensor (temperature/humidity/co2): ").lower()
            field_map = {"temperature": "field1", "humidity": "field2", "co2": "field3"}
            if sensor in field_map:
                display_historical(field_map[sensor])
            else:
                print("❌ Invalid sensor type.")
        elif choice == "3":
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    menu()
