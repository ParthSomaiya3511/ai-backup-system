from app.security.malware_detector import detect_malware
from app.security.ransomware_detector import detect_ransomware
from app.security.anomaly_detector import detect_anomaly


def analyze_file(file_path: str):

    malware = detect_malware(file_path)

    ransomware = detect_ransomware(file_path)

    anomaly = detect_anomaly(file_path)

    return {
        "malware": malware,
        "ransomware": ransomware,
        "anomaly": anomaly
    }