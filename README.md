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
├── frontend/ # React admin dashboard
│ ├── public/
│ │ └── system-status.json # System utility writes here
│ ├── src/
│ │ ├── App.js
│ │ └── App.css
│ └── package.json
│
├── system-monitor/ # System utility scripts
│ ├── system_status_monitor.py
│ ├── windows_checks.py
│ ├── mac_checks.py
│ └── linux_checks.py
│
└── README.md


---

## Prerequisites

- Python 3.8+ installed on your machines
- Node.js & npm installed for frontend development
- Windows PowerShell available for Windows checks
- Linux/macOS: standard terminal/shell

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/syspulse-dashboard.git
cd syspulse-dashboard



---

## Prerequisites

- Python 3.8+ installed on your machines
- Node.js & npm installed for frontend development
- Windows PowerShell available for Windows checks
- Linux/macOS: standard terminal/shell

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/syspulse-dashboard.git
cd syspulse-dashboard

2. Setup System Utility
Navigate to the system-monitor folder:cd system-monitor

