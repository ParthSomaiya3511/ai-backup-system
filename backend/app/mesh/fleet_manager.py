from live_monitoring import (
    get_system_health
)

def get_fleet_summary():

    return {

        "online_devices": 25,

        "offline_devices": 2,

        "health":

        get_system_health()

    }