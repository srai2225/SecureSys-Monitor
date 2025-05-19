import subprocess
import re
import platform
import json
import requests

def check_disk_encryption():
    result = {"enabled": False, "method": "BitLocker"}
    try:
        out = subprocess.check_output(["manage-bde", "-status", "C:"], text=True)
        if "Protection On" in out:
            result["enabled"] = True
        percent = re.search(r"Percentage Encrypted:\s+(\d+)", out)
        if percent:
            result["percent_encrypted"] = int(percent.group(1))
    except:
        pass
    return result

def get_latest_windows_build():
    try:
        url = "https://raw.githubusercontent.com/arevindh/windows-version-info/main/windows-10.json"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return data.get("latest", {}).get("build", None)
    except:
        pass
    return None

def check_os_updates():
    result = {
        "up_to_date": True,
        "updates_available": 0,
        "current_version": platform.version(),
        "latest_version": None
    }

    try:
        ps = (
            "$s = New-Object -ComObject Microsoft.Update.Session;"
            "$u = $s.CreateUpdateSearcher();"
            "$r = $u.Search('IsInstalled=0');"
            "$r.Updates.Count"
        )
        out = subprocess.check_output(["powershell", "-Command", ps], text=True).strip()
        count = int(out) if out.isdigit() else 0
        result["updates_available"] = count
        result["up_to_date"] = count == 0
    except:
        pass

    result["latest_version"] = get_latest_windows_build() or result["current_version"]
    return result

def check_antivirus():
    result = {"installed": False}
    try:
        ps = (
            "Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct "
            "| Select-Object displayName,productState | ConvertTo-Json"
        )
        out = subprocess.check_output(["powershell", "-Command", ps], text=True)
        data = json.loads(out)
        if isinstance(data, list):
            av = data[0]
        else:
            av = data
        result["installed"] = True
        result["name"] = av.get("displayName", "Unknown")
        ps = int(av.get("productState", 0))
        result["state"] = "On" if (ps & 0x1000) else "Off"
        result["signatures"] = "UpToDate" if (ps & 0x0010) == 0 else "OutOfDate"
    except:
        pass
    return result

def check_inactivity_sleep():
    result = {
        "ac_timeout_minutes": None,
        "battery_timeout_minutes": None
    }

    try:
        output = subprocess.check_output(["powercfg", "/q"], text=True)

        # Match the correct sleep setting GUID block
        sleep_block = re.search(
            r"Subgroup GUID:.*?SUB_SLEEP.*?(?:\r?\n)+.*?Power Setting GUID: 29f6c1db-86da-48c5-9fdb-f2b67b1f44da(.*?)\r?\n\r?\n",
            output, re.IGNORECASE | re.DOTALL
        )

        if sleep_block:
            block = sleep_block.group(1)

            ac_match = re.search(r"Current AC Power Setting Index: 0x([0-9a-fA-F]+)", block)
            dc_match = re.search(r"Current DC Power Setting Index: 0x([0-9a-fA-F]+)", block)

            if ac_match:
                val = int(ac_match.group(1), 16)
                result["ac_timeout_minutes"] = val // 60

            if dc_match:
                val = int(dc_match.group(1), 16)
                result["battery_timeout_minutes"] = val // 60

    except Exception as e:
        result["error"] = str(e)

    return result
