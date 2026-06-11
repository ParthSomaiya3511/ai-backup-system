from ai.file_classifier import classify_file
from ai.importance_detector import calculate_importance


def analyze_file(path):

    file_type = classify_file(path)

    importance = calculate_importance(path)

    return {

        "file_type": file_type,
        "importance": importance

    }