
# SecureSys Monitor

![Website Screenshot](https://i.postimg.cc/ZqR34D2Z/Screenshot-2025-05-20-004909.png)




SecureSys Monitor is a cross-platform system health monitoring utility with an intuitive admin dashboard. It collects key system data from Windows, macOS, and Linux machines, including disk encryption status, OS updates, antivirus presence, and inactivity sleep settings. The data is presented in a clean React web UI with filtering, dark mode, and CSV export features for easy administration.


## Features

- Cross-platform system utility (Windows/macOS/Linux)
- Checks disk encryption, OS update status, antivirus, and sleep timeout
- Runs as a background daemon (manual or scheduled)
- Cross platform
- Outputs JSON status read by React admin dashboard
- Dark/Light mode avialable
- React frontend with:
    - Machine list and details
    - Filtering by OS type
    - Export system data as CSV
- Modular and extensible architecture



## 📁 Repository Structure

```text
/                       # Root directory
├── frontend/           # React admin dashboard
│   ├── public/
│   │   └── system-status.json    # System utility writes here
│   ├── src/
│   │   ├── App.js
│   │   └── App.css
│   └── package.json
│
├── system-monitor/     # System utility scripts
│   ├── system_status_monitor.py
│   ├── windows_checks.py
│   ├── mac_checks.py
│   └── linux_checks.py
│
└── README.md

```


## Installation

1. Clone the Repository

```bash
  git clone https://github.com/yourusername/syspulse-dashboard.git
cd syspulse-dashboard

```
2. Setup System Utility
Navigate to the system-monitor folder:

```bash
  cd system-monitor

```
Install Python dependencies:
```bash
  pip install requests

```
3. Setup Frontend Dashboard
In a new terminal, navigate to the frontend folder:
```bash
  cd ../frontend

```
Install Node dependencies:
```bash
  npm install

```
Running the System Utility
Run Once (manual check)
```bash
  python system_status_monitor.py --once


```
This will:

Detect your OS

Run all system checks

Write JSON output to frontend/public/system-status.json



Run as Daemon (periodic check every 30 minutes)
```bash
  python system_status_monitor.py --daemon 1800

```
You can adjust the interval (in seconds).



Scheduling (Optional)
Windows: Use Task Scheduler to run the utility periodically.

Linux: Use systemd timer (see systemd setup below).

macOS: Use launchd agents to schedule the script.

Linux systemd setup

Create /etc/systemd/system/system-health.service with:

```bash
  [Unit]
Description=System Health Monitor

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /path/to/system-monitor/system_status_monitor.py --once


```

Create /etc/systemd/system/system-health.timer with:

```bash
[Unit]
Description=Run System Health Monitor every 30 minutes

[Timer]
OnBootSec=2min
OnUnitActiveSec=30min
Unit=system-health.service

[Install]
WantedBy=timers.target


```
Enable timer with:
```bash
sudo systemctl daemon-reexec
sudo systemctl enable --now system-health.timer


```
Running the Frontend Dashboard
From the frontend directory:
```bash
  npm start

```
## Troubleshooting

- Ensure Python and Node.js versions are compatible.

- On Windows, PowerShell must be enabled and accessible.

- If JSON file is not updating, check file permissions.

- For cross-platform daemon scheduling, consult OS-specific tools.
## Contact

- For questions or contributions, contact Sumit Rai at raisumit2225@gmail.com .


