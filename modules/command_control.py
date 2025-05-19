"""
Command & Control (C2) Simulation Module

Emulates attacker-controlled infrastructure (e.g., DNS tunneling) and logs beaconing activities.
"""

import json
import datetime

def simulate_command_control():
    c2_data = {
        "phase": "Command & Control",
        "description": "Simulated C2 beacon using DNS tunneling.",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "c2_method": "DNS Tunneling",
        "details": "Beacon sent to malicious DNS server"
    }
    log_attack(c2_data)
    return c2_data

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
    result = simulate_command_control()
    print("Command & Control simulation complete. Logged data:")
    print(json.dumps(result, indent=2))
