from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "ai-backup-secret"

ALGORITHM = "HS256"


def create_token(email):

    payload = {

        "sub": email,

        "exp":
        datetime.utcnow()
        + timedelta(hours=12)

    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )