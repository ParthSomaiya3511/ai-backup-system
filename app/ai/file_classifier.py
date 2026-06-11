import os

DOCUMENTS = [
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".xlsx"
]

IMAGES = [
    ".jpg",
    ".jpeg",
    ".png"
]

VIDEOS = [
    ".mp4",
    ".avi",
    ".mkv"
]

CODE = [
    ".py",
    ".js",
    ".java",
    ".php"
]


def classify_file(path):

    ext = os.path.splitext(path)[1].lower()

    if ext in DOCUMENTS:
        return "DOCUMENT"

    if ext in IMAGES:
        return "IMAGE"

    if ext in VIDEOS:
        return "VIDEO"

    if ext in CODE:
        return "CODE"

    return "OTHER"