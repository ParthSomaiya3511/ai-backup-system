from fastapi import APIRouter
from app.mesh.device_agent import get_device_info

router = APIRouter()

@router.get("/devices")

def devices():

    return [

        {

            "hostname":

            "Laptop-01",

            "status":

            "ONLINE"

        }

    ]