# SysPulse Dashboard

**SysPulse Dashboard** is a cross-platform system health monitoring utility with an intuitive admin dashboard. It collects key system data from Windows, macOS, and Linux machines, including disk encryption status, OS updates, antivirus presence, and inactivity sleep settings. The data is presented in a clean React web UI with filtering, dark mode, and CSV export features for easy administration.

---

## Features

- Cross-platform system utility (Windows/macOS/Linux)
- Checks disk encryption, OS update status, antivirus, and sleep timeout
- Runs as a background daemon (manual or scheduled)
- Outputs JSON status read by React admin dashboard
- React frontend with:
  - Machine list and details
  - Filtering by OS type
  - Dark mode toggle
  - Export system data as CSV
- Modular and extensible architecture

---

## Repository Structure
/
SecureSys-Monitor/
│
├── frontend/                  # React admin dashboard
│   ├── public/
│   └── src/
│       ├── App.js
│       └── App.css
│   └── package.json
│
├── system-monitor/           # System utility scripts
│   ├── system_status_monitor.py
│   ├── windows_checks.py
│   ├── mac_checks.py
│   └── linux_checks.py
│
├── system-status.json        # System utility writes here
└── README.md



---

⚙️ Prerequisites
Python 3.8+ installed on your machines

Node.js & npm installed for frontend development

Windows PowerShell available for Windows checks

Linux/macOS: standard terminal/shell

🔧 Setup & Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/syspulse-dashboard.git
cd syspulse-dashboard
2. Setup System Utility
Navigate to the system-monitor folder:

bash
Copy
Edit
cd system-monitor
Install Python dependencies:

bash
Copy
Edit
pip install requests
3. Setup Frontend Dashboard
In a new terminal, navigate to the frontend folder:

bash
Copy
Edit
cd ../frontend
Install Node dependencies:

bash
Copy
Edit
npm install
⚙️ Running the System Utility
➤ Run Once (Manual Check)
bash
Copy
Edit
python system_status_monitor.py --once
This will:

Detect your OS

Run all system checks

Write JSON output to frontend/public/system-status.json

➤ Run as Daemon (Periodic Check Every 30 Minutes)
bash
Copy
Edit
python system_status_monitor.py --daemon 1800
You can adjust the interval (in seconds).

🕒 Scheduling (Optional)
Windows: Use Task Scheduler to run the utility periodically

Linux: Use systemd timer (see example below)

macOS: Use launchd agents to schedule the script

🛠️ Example Linux systemd Setup
Create /etc/systemd/system/system-health.service with:

ini
Copy
Edit
[Unit]
Description=System Health Monitor

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /path/to/system-monitor/system_status_monitor.py --once
Create /etc/systemd/system/system-health.timer with:

ini
Copy
Edit
[Unit]
Description=Run System Health Monitor every 30 minutes

[Timer]
OnBootSec=2min
OnUnitActiveSec=30min
Unit=system-health.service

[Install]
WantedBy=timers.target
Enable the timer:

bash
Copy
Edit
sudo systemctl daemon-reexec
sudo systemctl enable --now system-health.timer
🖥️ Running the Frontend Dashboard
From the frontend directory:

bash
Copy
Edit
npm start
The React app will open in your browser at http://localhost:3000.

The dashboard reads system-status.json and displays system info live.

Use the filter dropdown, toggle dark mode, or export data as CSV.

📘 Usage
Run the utility on each client machine to update its status

The dashboard reads the combined JSON file to show all machines

Use filter dropdown to show specific OS machines

Use "Export to CSV" to download the current filtered data

Toggle between Light/Dark mode for comfort

📈 Extending the Project
Add backend API to collect reports centrally

Implement push notifications for critical issues

Add more system checks (CPU load, memory, disk space)

Improve UI with charts and historical trends

🐞 Troubleshooting
Ensure Python and Node.js versions are compatible

On Windows, PowerShell must be enabled and accessible

If JSON file is not updating, check file permissions

For cross-platform daemon scheduling, consult OS-specific tools

📝 License
MIT License

📬 Contact
For questions or contributions, contact [Your Name] at [your.email@example.com].
