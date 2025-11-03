import re
import json
from datetime import datetime

def parse_usbstor(raw_text):
    # Extract device name
    name_match = re.search(r'Device Name:\s*(.+)', raw_text)
    device_name = name_match.group(1).strip() if name_match else "Unknown"

    # Extract serial number
    serial_match = re.search(r'Serial Number:\s*(.+)', raw_text)
    serial_number = serial_match.group(1).strip() if serial_match else "Unknown"

    # Extract first connected time
    time_match = re.search(r'First Connected:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', raw_text)
    if time_match:
        first_connected = datetime.strptime(time_match.group(1), "%Y-%m-%d %H:%M:%S").isoformat() + "Z"
    else:
        first_connected = "Unknown"

    parsed = {
        "artifact_type": "USBSTOR",
        "device_name": device_name,
        "serial_number": serial_number,
        "first_connected": first_connected
    }

    return json.dumps(parsed, indent=2)