from fastapi import APIRouter

router = APIRouter()

devices = []


@router.get("/devices")

def get_devices():

    return devices

    
@router.post("/devices")

def create_device(device:dict):

    devices.append(device)

    return {

        "success": True

    }