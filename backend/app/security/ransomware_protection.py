from security.threat_database import (
    RANSOMWARE_EXTENSIONS
)

def detect_ransomware(file_path):

    for ext in RANSOMWARE_EXTENSIONS:

        if file_path.lower().endswith(ext):

            return True

    return False