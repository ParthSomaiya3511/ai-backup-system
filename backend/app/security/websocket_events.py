from fastapi import WebSocket

connections = []

async def connect(

    websocket: WebSocket

):

    await websocket.accept()

    connections.append(websocket)
    
    
async def broadcast(message):

    for connection in connections:

        await connection.send_json(
            message
        )