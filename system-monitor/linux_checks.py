import subprocess, shutil, re, platform

def check_disk_encryption():
    result = {"enabled": False, "method": None}
    try:
        out = subprocess.check_output(["lsblk", "-o", "TYPE"], text=True)
        if "crypt" in out:
            result["enabled"] = True
            result["method"] = "LUKS"
    except:
        pass
    return result

def check_os_updates():
    result = {"up_to_date": True, "updates_available": 0}
    try:
        if shutil.which("apt-get"):
            out = subprocess.check_output(["apt-get", "-s", "upgrade"], text=True)
            result["updates_available"] = len([l for l in out.splitlines() if l.startswith("Inst")])
            result["up_to_date"] = result["updates_available"] == 0
        result["current_version"] = platform.platform()
    except:
        pass
    return result

def check_antivirus():
    names = ["clamd", "freshclam", "csagent"]
    for name in names:
        try:
            subprocess.check_output(["pgrep", name])
            return {"installed": True, "name": name, "state": "Running"}
        except:
            continue
    return {"installed": False}

def check_inactivity_sleep():
    result = {}
    try:
        with open("/etc/systemd/logind.conf") as f:
            for line in f:
                if "IdleActionSec" in line:
                    val = line.split("=")[1].strip()
                    if val.endswith("min"):
                        val = int(val.replace("min", ""))
                        result["ac_timeout_minutes"] = result["battery_timeout_minutes"] = val
    except:
        result["ac_timeout_minutes"] = result["battery_timeout_minutes"] = 0
    return result
