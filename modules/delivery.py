"""
Delivery Module

Simulates the delivery of payloads via email or web download.
Logs the delivery attempt for SOC analysis.
"""

import json
import datetime

def simulate_delivery():
    delivery_data = {
        "phase": "Delivery",
        "description": "Simulated payload delivery via phishing email.",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "delivery_method": "Email",
        "email_details": {
            "sender": "attacker@example.com",
            "receiver": "victim@example.com",
            "attachment": "malicious.doc"
        }
    }
    log_attack(delivery_data)
    return delivery_data

def log_attack(data):
    log_file = "../logs/attack_logs.json"
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
    logs.append(data)
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)

if __name__ == "__main__":
    result = simulate_delivery()
    print("Delivery simulation complete. Logged data:")
    print(json.dumps(result, indent=2))
