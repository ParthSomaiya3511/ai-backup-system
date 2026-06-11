def detect_anomaly(event_count):

    if event_count > 500:
        return True

    return False