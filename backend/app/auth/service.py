from app.auth.jwt_handler import create_token


def login_user(email: str, password: str):

    if (
        email == "admin@amdox.com"
        and
        password == "admin123"
    ):

        return {
            "success": True,
            "token": create_token(email),
            "user": {
                "email": email,
                "role": "Administrator"
            }
        }

    return {
        "success": False,
        "message": "Invalid email or password"
    }