SUSPICIOUS_EXTENSIONS = [
    "locked",
    "encrypted",
    "crypt",
    "locky"
]


def detect_ransomware(file_path: str) -> dict:

    extension = file_path.split(".")[-1].lower()

    if extension in SUSPICIOUS_EXTENSIONS:
        return {
            "detected": True,
            "severity": "Critical"
        }

    return {
        "detected": False,
        "severity": "Safe"
    }