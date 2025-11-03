import re
import json
from datetime import datetime

def parse_mft(raw_text):
    # Extract file name
    name_match = re.search(r'File Name:\s*(.+)', raw_text)
    file_name = name_match.group(1).strip() if name_match else "Unknown"

    # Extract file path
    path_match = re.search(r'File Path:\s*(.+)', raw_text)
    file_path = path_match.group(1).strip() if path_match else "Unknown"

    # Extract timestamps
    def extract_time(label):
        match = re.search(fr'{label}:\s*(\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}})', raw_text)
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S").isoformat() + "Z" if match else "Unknown"

    created = extract_time("Created")
    modified = extract_time("Modified")
    accessed = extract_time("Accessed")

    # Extract file size
    size_match = re.search(r'File Size:\s*(\d+)', raw_text)
    file_size = int(size_match.group(1)) if size_match else 0

    # Extract deletion status
    deleted_match = re.search(r'Deleted:\s*(True|False)', raw_text)
    deleted = deleted_match.group(1) == "True" if deleted_match else False

    # Build structured output
    parsed = {
        "artifact_type": "$MFT",
        "file_name": file_name,
        "file_path": file_path,
        "created": created,
        "modified": modified,
        "accessed": accessed,
        "file_size": file_size,
        "deleted": deleted
    }

    return json.dumps(parsed, indent=2)

if __name__ == "__main__":
    raw_mft = (
        "File Name: report.docx\n"
        "File Path: C:\\Users\\Warren\\Documents\\report.docx\n"
        "Created: 2023-08-01 10:15:00\n"
        "Modified: 2023-08-02 14:30:00\n"
        "Accessed: 2023-08-02 14:30:00\n"
        "File Size: 24576\n"
        "Deleted: False"
    )

    result = parse_mft(raw_mft)
    print("Parsed Output:")
    print(result)