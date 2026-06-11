from auth.jwt_handler import create_token

def login_user(
    email,
    password
):

    if (
        email == "admin@amdox.com"
        and
        password == "admin123"
    ):

        return {

            "token":
            create_token(email)

        }

    return None