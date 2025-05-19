"""
Reconnaissance Module

Simulates OSINT techniques used by attackers (e.g., WHOIS lookups, subdomain enumeration, email harvesting) and logs the findings.
"""

import json
import datetime

def simulate_reconnaissance():
    recon_data = {
        "phase": "Reconnaissance",
        "description": "Conducted WHOIS lookup and subdomain enumeration.",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "results": {
            "domain": "example.com",
            "subdomains": ["shop.example.com", "blog.example.com"],
            "registrant": "John Doe",
            "emails": ["contact@example.com", "support@example.com"]
        }
    }
    log_attack(recon_data)
    return recon_data

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
    result = simulate_reconnaissance()
    print("Reconnaissance simulation complete. Logged data:")
    print(json.dumps(result, indent=2))
