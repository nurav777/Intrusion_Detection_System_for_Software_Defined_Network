# 🛡️ SDN-Based Network Intrusion Detection System (IDS)

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)  
[![Mininet](https://img.shields.io/badge/Mininet-2.3.0-green)](http://mininet.org/)  
[![POX](https://img.shields.io/badge/POX-SDN-orange)](https://github.com/noxrepo/pox)

---

## 📖 Overview

This project implements a **real-time Network Intrusion Detection and Prevention System (IDPS)** using **Software Defined Networking (SDN)**.  

✨ **Key Features:**

- 🔍 Real-time traffic monitoring using **Scapy**  
- 🧠 Traffic classification with a **Random Forest ML model**  
- 🚫 Automatic blocking of malicious IPs via `iptables`  
- 📱 Real-time alerts via **Telegram bot**  
- 🌐 Simulated network topology using **Mininet** and **POX SDN controller**  

This modular design ensures **scalability**, **responsiveness**, and **enhanced network security**.

---

## 📂 Project Structure

**SDN_IDS_Project/**

- `src/` – Source code
  - `custom_topology.py` – Mininet topology setup
  - `train_model.py` – ML model training
  - `traffic_analysis.py` – Traffic sniffing & IDS
  - `notifier.py` – Telegram alert bot
- `screenshots/` – Terminal outputs & demos
- `ml_models/` – Trained ML models (`.pkl`)
- `README.md` – Project documentation

---

## 🛠️ Requirements

- Linux environment 🐧  
- Python 3.x 🐍  
- Mininet  
- POX SDN controller  
- Python packages:
  - scapy  
  - numpy  
  - scikit-learn  
  - joblib  
  - python-telegram-bot  
  - nest_asyncio  
- hping3 (for attack simulation)  
- iptables (for automated blocking)  

---

## 🚀 How to Run

### 1️⃣ Start the POX Controller

`./pox.py forwarding.l2_learning`

---

### 2️⃣ Launch Mininet Custom Topology

`sudo python3 src/custom_topology.py`

Inside Mininet CLI, start an HTTP server on `h1`:

`h1 python3 -m http.server 80`

---

### 3️⃣ Train the ML Traffic Classifier (Optional)

`python3 src/train_model.py`  

Generates `ml_traffic_classifier.pkl` ✅

---

### 4️⃣ Run Traffic Analysis & IDS

`python3 src/traffic_analysis.py`  

- Monitors traffic  
- Classifies packets  
- Blocks harmful IPs  
- Logs events  

---

### 5️⃣ Start Telegram Notifier

`python3 src/notifier.py`  

- Sends alerts for blocked IPs 📩  
- Handles `/unblock` commands 🔄  

---

## 💻 Demonstration

### Normal Traffic

`h2 wget http://10.0.0.1`  

- Classified as **Harmless** ✅  
- Logged in `traffic_log.txt` 📄  

### Malicious Traffic Simulation

`h2 hping3 --udp -p 80 --flood 10.0.0.1`  

- Classified as **Harmful** ⚠️  
- IP blocked automatically 🚫  
- Telegram alert sent to admin 📱  

### Unblocking

- Admin sends `/unblock` via Telegram  
- IP restriction removed 🔓  
- H2 can access H1 again 🌐  

---

## 🔧 Modules

1. **Mininet Topology Setup** 🌐 – Builds the virtual network  
2. **POX SDN Controller** 🖥️ – Dynamic flow control & MAC learning  
3. **Intrusion Detection System (IDS)** 🧠 – Classifies traffic with ML  
4. **Real-Time Alerting & Logging** 📄 – Logs events & sends Telegram alerts  
5. **Automated IP Blocking** 🚫 – Blocks malicious IPs instantly  

---

## 📊 Comparative Advantages

| Feature | Traditional IDS | This Project |
|---------|----------------|--------------|
| Detection | Signature-based | ML-based (Random Forest) |
| Response | Passive logging | Active IP blocking |
| Network Control | Static, limited | SDN-based, programmable |
| Alerts | CLI logs | Real-time Telegram notifications |
| Traffic Simulation | Ping/iperf | Mininet + hping3 |

---

## ✅ Conclusion

This project demonstrates a **scalable, intelligent, and proactive SDN-based IDS**, combining:

- 🔍 **Real-time traffic monitoring**  
- 🧠 **Machine learning for anomaly detection**  
- 🚫 **Automated IP blocking**  
- 📱 **Telegram bot integration for alerts and control**  

It provides a **robust foundation for modern network security** and is fully expandable for larger SDN environments.

---

## 📸 Screenshots

Terminal screenshots included in `/screenshots` to visually demonstrate:

- POX controller running  
- Mininet topology  
- wget requests & logs  
- Telegram alerts  
- Attack simulation with hping3  
- IP blocking & unblocking  

