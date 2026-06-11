from fastapi import APIRouter

from mesh.heartbeat_manager import (
    update_heartbeat
)

router = APIRouter()

@router.post(
    "/heartbeat/{device_id}"
)
def heartbeat(
    device_id
):

    update_heartbeat(
        device_id
    )

    return {

        "success": True

    }   