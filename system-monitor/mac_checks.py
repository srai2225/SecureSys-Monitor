import subprocess, platform, re

def check_disk_encryption():
    result = {"enabled": False, "method": "FileVault"}
    try:
        out = subprocess.check_output(["fdesetup", "status"], text=True)
        if "On" in out:
            result["enabled"] = True
    except:
        pass
    return result

def check_os_updates():
    result = {"up_to_date": True, "updates_available": 0}
    try:
        out = subprocess.check_output(["softwareupdate", "-l"], text=True)
        result["updates_available"] = sum(1 for line in out.splitlines() if line.strip().startswith("*"))
        result["up_to_date"] = result["updates_available"] == 0
    except:
        pass
    result["current_version"] = platform.mac_ver()[0]
    return result

def check_antivirus():
    known = ["ClamXAV", "Sophos", "Avast"]
    for name in known:
        try:
            out = subprocess.check_output(["pgrep", "-f", name], text=True)
            if out:
                return {"installed": True, "name": name, "state": "Running"}
        except:
            continue
    return {"installed": False}

def check_inactivity_sleep():
    result = {}
    try:
        out = subprocess.check_output(["pmset", "-g", "custom"], text=True)
        ac = re.search(r"AC Power.*sleep\s+(\d+)", out)
        bat = re.search(r"Battery Power.*sleep\s+(\d+)", out)
        if ac:
            result["ac_timeout_minutes"] = int(ac.group(1))
        if bat:
            result["battery_timeout_minutes"] = int(bat.group(1))
    except:
        pass
    return result
