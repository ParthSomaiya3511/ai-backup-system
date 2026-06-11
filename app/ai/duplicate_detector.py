import hashlib

def generate_hash(path):

    hasher = hashlib.sha256()

    with open(path, "rb") as file:

        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()