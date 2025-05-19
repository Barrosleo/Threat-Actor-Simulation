"""
Installation Module

Simulates the installation of a payload (e.g., creating persistence)
and logs the installation activity.
"""

import json
import datetime

def simulate_installation():
    installation_data = {
        "phase": "Installation",
        "description": "Simulated persistence mechanism installation.",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "method": "Modified startup registry entry"
    }
    log_attack(installation_data)
    return installation_data

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
    result = simulate_installation()
    print("Installation simulation complete. Logged data:")
    print(json.dumps(result, indent=2))
