import os

def file_exists(path):

    return os.path.exists(path)

def file_corrupted(path):

    try:
        with open(path, "rb") as f:
            f.read(1024)

        return False

    except Exception:
        return True