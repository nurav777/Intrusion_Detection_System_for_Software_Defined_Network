🛡️ SDN-Based Network Intrusion Detection System (IDS)






📖 Overview

This project implements a real-time Network Intrusion Detection and Prevention System (IDPS) using Software Defined Networking (SDN).

Key features:

Monitors network traffic in real-time using Scapy

Classifies traffic with a Random Forest ML model

Automatically blocks malicious IPs using iptables

Sends real-time alerts via Telegram bot

Simulates network topology using Mininet with the POX SDN controller

This modular design ensures scalability, responsiveness, and enhanced network security.

📂 Project Structure

SDN_IDS_Project/

src/ – Source code

custom_topology.py

train_model.py

traffic_analysis.py

notifier.py

screenshots/ – Terminal screenshots & outputs

pox_controller.png

mininet_topology.png

wget_demo.png

telegram_alert.png

ml_models/ – Pretrained ML models

ml_traffic_classifier.pkl

README.md – Project documentation

🛠️ Requirements

Linux environment

Python 3.x

Mininet

POX SDN controller

Python packages:

scapy

numpy

scikit-learn

joblib

python-telegram-bot

nest_asyncio

hping3 (for attack simulation)

iptables (for automated blocking)

🚀 How to Run
1️⃣ Start the POX Controller

Navigate to POX folder and run:

./pox.py forwarding.l2_learning

2️⃣ Launch Mininet Custom Topology

sudo python3 src/custom_topology.py

Inside Mininet CLI, start an HTTP server on h1:

h1 python3 -m http.server 80

3️⃣ Train the ML Traffic Classifier (Optional)

python3 src/train_model.py

Generates ml_traffic_classifier.pkl

4️⃣ Run Traffic Analysis & IDS

python3 src/traffic_analysis.py

Monitors traffic, classifies packets, blocks harmful IPs, logs events

5️⃣ Start Telegram Notifier

python3 src/notifier.py

Sends alerts for blocked IPs

Handles /unblock commands

💻 Demonstration
Normal Traffic

h2 wget http://10.0.0.1

Classified as Harmless

Logs updated in traffic_log.txt

Malicious Traffic Simulation

h2 hping3 --udp -p 80 --flood 10.0.0.1

Classified as Harmful

IP blocked automatically

Telegram alert sent to admin

Unblocking

Admin sends /unblock via Telegram

IP restriction removed

H2 can access H1 again

🔧 Modules

Mininet Topology Setup – Builds the virtual network

POX SDN Controller – Dynamic flow control & MAC learning

Intrusion Detection System (IDS) – Classifies traffic with ML

Real-Time Alerting & Logging – Logs events & sends Telegram alerts

Automated IP Blocking – Blocks malicious IPs instantly
