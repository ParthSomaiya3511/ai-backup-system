from fastapi import WebSocket

class ConnectionManager:

    def __init__(self):

        self.connections = {}

    async def connect(
        self,
        device_id,
        websocket: WebSocket
    ):

        await websocket.accept()

        self.connections[
            device_id
        ] = websocket

    def disconnect(
        self,
        device_id
    ):

        if device_id in self.connections:

            del self.connections[
                device_id
            ]

manager = ConnectionManager()



async def send_command(
    device_id,
    command
):

    if device_id not in manager.connections:

        return False

    await manager.connections[
        device_id
    ].send_json({

        "command": command

    })

    return True