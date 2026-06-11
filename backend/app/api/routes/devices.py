from fastapi import APIRouter

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