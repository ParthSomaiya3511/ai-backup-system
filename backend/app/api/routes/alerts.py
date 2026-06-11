from fastapi import APIRouter

router = APIRouter()

@router.get("/alerts")

def alerts():

    return {

        "active_alerts": 3

    }