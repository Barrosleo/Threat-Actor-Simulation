# Threat Actor Simulation & Detection Toolkit

## Purpose
Develop a tool that simulates various attack techniques across the Cyber Kill Chain phases and provides detection strategies for SOC analysts. This project allows you to understand adversary tactics and improve incident response by simulating the full attack lifecycle.

## Key Features
- **Reconnaissance Module:**  
  Simulates OSINT activities (WHOIS, subdomain enumeration, email harvesting) and logs the gathered intelligence.
- **Weaponization & Delivery Module:**  
  Creates harmless test payloads and simulates phishing email and document delivery scenarios.
- **Exploitation & Installation Module:**  
  Demonstrates common exploitation methods (e.g., buffer overflow) and simulates persistence mechanisms.
- **Command & Control (C2) Simulation:**  
  Emulates attacker-controlled infrastructure (e.g., DNS tunneling) and provides detection rules.
- **Exfiltration & Actions on Objectives:**  
  Simulates data exfiltration methods (e.g., encrypted transfers) and generates alerts for investigation.

## Tech Stack
- **Backend:** Python with Flask (for simulation and logging)
- **Frontend:** Simple web dashboard using HTML, CSS, and JavaScript (with Chart.js for visualization)
- **Data Integration:** Logs formatted for SIEM ingestion

## Repository Structure
```
Threat-Actor-Simulation/
├── modules/
│   ├── reconnaissance.py
│   ├── weaponization.py
│   ├── delivery.py
│   ├── exploitation.py
│   ├── installation.py
│   ├── command_control.py
│   └── exfiltration.py
├── dashboard/
│   ├── index.html
│   ├── styles.css
│   └── dashboard.js
├── logs/
│   ├── attack_logs.json
│   └── detection_rules.txt
├── README.md
```

## How to Run
1. **Backend Simulation:**  
   Navigate to the `modules/` directory and run the Python modules individually to simulate each attack phase. Each module will append simulated attack data to `logs/attack_logs.json`.

2. **Dashboard:**  
   Open the `dashboard/index.html` file in your web browser. The dashboard fetches the attack logs and displays a visual summary using Chart.js.

## Future Enhancements
- **SIEM Integration:** Pre-built detection rules for platforms like Splunk or ELK.
- **Automated Reporting:** Generate PDF reports for SOC teams.
- **Red Team vs. Blue Team Mode:** Enable simulation of interactive attack and defense scenarios.

## License
This project is licensed under the MIT License.




