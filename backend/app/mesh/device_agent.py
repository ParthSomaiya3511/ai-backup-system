import socket
import uuid

def get_device_info():

    return {

        "device_id":

        str(uuid.uuid4()),

        "hostname":

        socket.gethostname()

    }