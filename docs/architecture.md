# Architecture Overview

## System Components

1. **Backend (Python):**
   - Each module in the `modules/` directory simulates an attack phase and logs details to `logs/attack_logs.json`.
   - Example phases include Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, and Exfiltration.

2. **Frontend (Dashboard):**
   - `index.html` offers a basic web interface.
   - `dashboard.js` fetches attack logs and renders a bar chart using Chart.js.
   - `styles.css` provides styling for a clean dashboard layout.

3. **Logs & Detection Rules:**
   - `logs/attack_logs.json` stores all simulated attack events.
   - `logs/detection_rules.txt` contains detection strategies and rules for SOC teams.

## Data Flow
1. Simulation modules generate and log attack data.
2. The dashboard fetches the logged data and visualizes the information.
3. This setup can later be integrated into a SIEM platform or enhanced with threat intelligence APIs.
