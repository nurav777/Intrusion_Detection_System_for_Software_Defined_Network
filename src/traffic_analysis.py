import time
import os
import joblib
import threading
from scapy.all import sniff, IP, UDP

log_file = "traffic_log.txt"
model_path = "ml_traffic_classifier.pkl"


blocked_ips = set()
ip_packet_times = {}  # for packet rate tracking

# Load model
model = joblib.load(model_path)

#  Extract required features
def extract_features(packet):
    pkt_len = len(packet)
    ttl = packet[IP].ttl if packet.haslayer(IP) else 0
    is_udp = int(packet.haslayer(UDP))

    # Track packet rate
    now = time.time()
    src_ip = packet[IP].src if packet.haslayer(IP) else "unknown"
    ip_packet_times.setdefault(src_ip, []).append(now)

    # Keep timestamps only from last second
    ip_packet_times[src_ip] = [t for t in ip_packet_times[src_ip] if now - t <= 1]
    pkt_rate = len(ip_packet_times[src_ip])

    return [pkt_len, ttl, is_udp, pkt_rate]

# Classify packet with ML
def classify_packet(packet):
    if not packet.haslayer(IP):
        return "Harmless", None

    features = extract_features(packet)
    prediction = model.predict([features])[0]  # 'Harmless' or 'Harmful'
    return prediction, packet[IP].src

#  Block IP if malicious
def block_ip(ip):
    if ip in blocked_ips:
        return

    command = f"h1 sudo iptables -A INPUT -s {ip} -j DROP"
    os.system(command)
    blocked_ips.add(ip)

    with open(log_file, "a") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] [BLOCKED] {ip} has been blocked by iptables\n")

# Unblock all blocked IPs
def unblock_all_ips():
    global blocked_ips
    for ip in list(blocked_ips):
        os.system(f"h1 sudo iptables -D INPUT -s {ip} -j DROP")
        print(f" Unblocked: {ip}")
        blocked_ips.remove(ip)

    with open(log_file, "a") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] [INFO] All IPs have been unblocked.\n")

# Watch traffic_log.txt for unblock command
def watch_log_for_unblock():
    seen_lines = set()
    while True:
        try:
            with open(log_file, "r") as f:
                lines = f.readlines()

            for line in lines:
                if line not in seen_lines:
                    seen_lines.add(line)
                    if "[CMD] UNBLOCK_ALL" in line:
                        unblock_all_ips()

            time.sleep(1)
        except Exception as e:
            print(f"[ERROR] Watching log failed: {e}")
            time.sleep(2)

# Main logging & detection logic
def log_packet(packet):
    label, src_ip = classify_packet(packet)

    if src_ip:
        with open(log_file, "a") as f:
            f.write(f"[{time.strftime('%H:%M:%S')}] Packet from {src_ip} classified as {label}\n")

        if label == "Harmful":
            block_ip(src_ip)

# Start sniffing and unblock thread
if __name__ == "__main__":
    print(" Monitoring traffic using ML model...")

    # Start background thread for unblock command
    threading.Thread(target=watch_log_for_unblock, daemon=True).start()

    sniff(prn=log_packet, store=0)
