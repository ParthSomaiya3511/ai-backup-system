from datetime import datetime, timedelta

import jwt


SECRET_KEY = "amdox-ai-backup-secret"

ALGORITHM = "HS256"


def create_token(email: str):

    payload = {

        "sub": email,

        "exp": datetime.utcnow() + timedelta(hours=12)

    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )