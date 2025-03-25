
# 🌱 CIS600 - IoT Assignment 3 (Spring 2025)

This project implements a cloud-based IoT system that simulates environmental stations and publishes sensor data (temperature, humidity, CO₂) using the MQTT protocol. The data is forwarded to ThingSpeak for visualization and retrieved later via its Read API.

---

## 🛠️ Components

### 1. `sensor-simulator.py`
Simulates a virtual IoT station that:
- Generates random temperature, humidity, and CO₂ values
- Publishes data every few seconds via MQTT to `mqtt.eclipseprojects.io`

### 2. `thingspeak.py`
- Subscribes to the MQTT topic
- Receives sensor data
- Sends data to **ThingSpeak** using the Write API key (HTTP)

### 3. `thingspeak_reader.py`
- CLI tool to **read data back** from ThingSpeak using the Read API
- Supports:
  - Viewing the **latest sensor readings**
  - Displaying **last 5 hours of data** for a specific sensor
  - Optional matplotlib plots for data trends

---

## 🔁 Data Flow

```
[Sensor Simulator] --> (MQTT) --> [ThingSpeak Forwarder] --> (HTTP) --> [ThingSpeak Channel]
                                                                 ↓
                                                    [Read API + CLI Viewer]
```

---

## 🚀 Installation

### 1. Clone the repo:
```bash
git clone https://github.com/SwarajSam98/iot-assignment3.git
cd iot-assignment3
```

### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run

Open **3 terminal windows** and run the following:

---

### 🧾 Terminal 1 – Simulate Sensor
```bash
python sensor-simulator.py
```

---

### 🌐 Terminal 2 – Forward to ThingSpeak
```bash
python thingspeak.py
```

---

### 📊 Terminal 3 – Read from ThingSpeak
```bash
python thingspeak_reader.py
```

---

💡 Make sure to update your ThingSpeak API keys and Channel ID in the respective scripts before running.

---

## 📊 ThingSpeak Setup

1. Create a new ThingSpeak channel
2. Enable 3 fields:
   - Field1 → Temperature
   - Field2 → Humidity
   - Field3 → CO₂
3. Paste the Write and Read API keys into:
   - `thingspeak.py` → `THINGSPEAK_API_KEY`
   - `thingspeak_reader.py` → `READ_API_KEY`, `CHANNEL_ID`

---

## 📷 Screenshots

- Sensor data publishing:
  ![image](https://github.com/user-attachments/assets/31b476b6-5753-4ef1-b9df-301125d545d5)


- ThingSpeak receiving data:
  ![image](https://github.com/user-attachments/assets/6e8c0723-8dff-4ba0-a958-7f899222432a)

- CLI menu fetching latest and historical data:
  ![image](https://github.com/user-attachments/assets/54260270-e6a7-4369-8d62-cf8c1d41b5ed)
  ![image](https://github.com/user-attachments/assets/c17e1e26-f98e-4866-8357-cc5561658f9b)
  
- ThingSpeak dashboard graphs:
  ![image](https://github.com/user-attachments/assets/a406b357-1c60-42c1-9b7f-942e1ba24fcf)

- matplotlib line charts:
- Temperature: ![image](https://github.com/user-attachments/assets/d73dde41-4452-4a92-a925-63fc2c18d807)
- Humidity: ![image](https://github.com/user-attachments/assets/5be9e58d-18d4-45ad-996d-30008499970c)
- CO2: ![image](https://github.com/user-attachments/assets/3070ce72-449f-4cf6-8120-9c06eb42bfc3)




---

## 🧠 Reflection

This project demonstrates the full IoT data flow from virtual sensing, through MQTT messaging, to cloud visualization and analysis. It uses lightweight protocols and cloud APIs commonly found in real-world IoT deployments.

---

## 📂 Files Included

| File                   | Description                                   |
|------------------------|-----------------------------------------------|
| `sensor-simulator.py`  | Simulates environmental data (Temp, Hum, CO₂) |
| `thingspeak.py`        | Forwards MQTT data to ThingSpeak              |
| `thingspeak_reader.py` | Reads and plots data from ThingSpeak          |
| `requirements.txt`     | Required libraries                            |
| `README.md`            | This file                                     |

---

## 🔗 Author

**Swaraj Santosh Sambare**  |  Spring 2025
