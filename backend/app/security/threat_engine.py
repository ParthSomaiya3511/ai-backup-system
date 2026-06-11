from security.malware_detector import (
    detect_malware
)

from security.ransomware_protection import (
    detect_ransomware
)

from security.quarantine_manager import (
    quarantine_file
)

def analyze_file(file_path):

    if detect_ransomware(file_path):

        return {

            "type":
            "RANSOMWARE",

            "severity":
            "CRITICAL"

        }

    if detect_malware(file_path):

        return {

            "type":
            "MALWARE",

            "severity":
            "HIGH"

        }

    return {

        "type":
        "SAFE",

        "severity":
        "NONE"

    }