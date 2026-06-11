import os

def calculate_importance(path):

    score = 0

    file_name = os.path.basename(path)

    if "project" in file_name.lower():
        score += 40

    if "final" in file_name.lower():
        score += 30

    if os.path.getsize(path) > 1000000:
        score += 20

    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "MEDIUM"

    return "LOW"