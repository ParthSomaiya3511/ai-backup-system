import secrets

def generate_reset_token():

    return secrets.token_hex(
        32
    )