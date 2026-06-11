from datetime import datetime

heartbeats = {}

def update_heartbeat(
    device_id
):

    heartbeats[
        device_id
    ] = datetime.now()
    
    
def get_last_seen(
    device_id
):

    return heartbeats.get(
        device_id
    )