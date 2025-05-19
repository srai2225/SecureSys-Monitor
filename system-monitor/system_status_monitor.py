import os
import platform
import json
from datetime import datetime, timezone
import sys

# Import OS-specific check modules
if platform.system() == "Windows":
    import windows_checks as checks
elif platform.system() == "Darwin":
    import mac_checks as checks
elif platform.system() == "Linux":
    import linux_checks as checks
else:
    checks = None

# Path to frontend/public/system-status.json
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "public", "system-status.json"))

def get_machine_id():
    return platform.node()

def run_checks_and_write():
    if not checks:
        print("[!] Unsupported OS or check module missing.")
        return

    machine_data = {
        "machine_id": get_machine_id(),
        "os": platform.system(),
        "last_checked": datetime.now(timezone.utc).isoformat(),
        "disk_encryption": checks.check_disk_encryption(),
        "os_updates": checks.check_os_updates(),
        "antivirus": checks.check_antivirus(),
        "inactivity_sleep": checks.check_inactivity_sleep()
    }

    # Read existing data (list of machines)
    try:
        with open(output_path, "r") as f:
            existing = json.load(f)
            if isinstance(existing, dict):
                existing = []  # legacy format fix
    except Exception:
        existing = []

    # Check if this machine's data has changed
    existing_dict = {entry["machine_id"]: entry for entry in existing}
    old_entry = existing_dict.get(machine_data["machine_id"])

    if old_entry != machine_data:
        updated = [e for e in existing if e["machine_id"] != machine_data["machine_id"]]
        updated.append(machine_data)
        with open(output_path, "w") as f:
            json.dump(updated, f, indent=2)
        print(f"[✓] Updated system status for {machine_data['machine_id']}.")
    else:
        print(f"[–] No changes for {machine_data['machine_id']}. Skipped write.")

if __name__ == "__main__":
    if "--once" in sys.argv:
        run_checks_and_write()
    elif "--daemon" in sys.argv:
        interval = 1800  # default 30 min
        try:
            interval_index = sys.argv.index("--daemon") + 1
            if interval_index < len(sys.argv):
                interval = int(sys.argv[interval_index])
        except:
            pass
        import time
        print(f"[~] Running in daemon mode every {interval} seconds...")
        while True:
            run_checks_and_write()
            time.sleep(interval)
    else:
        print("Usage:")
        print("  python system_status_monitor.py --once")
        print("  python system_status_monitor.py --daemon [seconds]")
