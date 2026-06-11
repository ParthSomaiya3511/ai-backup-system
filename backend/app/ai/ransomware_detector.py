SUSPICIOUS_EXTENSIONS = [

    ".locked",
    ".encrypted",
    ".crypt"

]

def is_suspicious(path):

    for ext in SUSPICIOUS_EXTENSIONS:

        if path.endswith(ext):
            return True

    return False