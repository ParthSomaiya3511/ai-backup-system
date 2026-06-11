def calculate_score(

    malware_count,

    ransomware_count,

    suspicious_events

):

    score = 100

    score -= malware_count * 10

    score -= ransomware_count * 25

    score -= suspicious_events * 5

    return max(score, 0)