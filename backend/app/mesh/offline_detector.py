from datetime import datetime

def is_offline(
    last_seen,
    timeout=120
):

    if last_seen is None:

        return True

    diff = (
        datetime.now()
        -
        last_seen
    ).seconds

    return diff > timeout