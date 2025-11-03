import re
import json
from datetime import datetime

def parse_amcache(raw_text):
    # Extract file path
    path_match = re.search(r'File Path:\s*(.+)', raw_text)
    file_path = path_match.group(1).strip() if path_match else "Unknown"

    # Extract SHA1
    sha_match = re.search(r'SHA1:\s*([A-Fa-f0-9]{40})', raw_text)
    sha1 = sha_match.group(1) if sha_match else "Unknown"

    # Extract execution time
    exec_match = re.search(r'First Execution Time:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', raw_text)
    if exec_match:
        dt = datetime.strptime(exec_match.group(1), "%Y-%m-%d %H:%M:%S")
        first_execution = dt.isoformat() + "Z"
    else:
        first_execution = "Unknown"

    # Extract publisher
    pub_match = re.search(r'Publisher:\s*(.+)', raw_text)
    publisher = pub_match.group(1).strip() if pub_match else "Unknown"

    # Build structured output
    parsed = {
        "artifact_type": "AmCache",
        "file_path": file_path,
        "sha1": sha1,
        "first_execution": first_execution,
        "publisher": publisher
    }

    return json.dumps(parsed, indent=2)

if __name__ == "__main__":
    raw_amcache = (
        "File Path: C:\\Program Files\\CCleaner\\CCleaner.exe\n"
        "SHA1: A1B2C3D4E5F67890ABCDEF1234567890ABCDEF12\n"
        "First Execution Time: 2023-09-15 08:22:00\n"
        "Publisher: Piriform Ltd"
    )

    result = parse_amcache(raw_amcache)
    print("Parsed Output:")
    print(result)


