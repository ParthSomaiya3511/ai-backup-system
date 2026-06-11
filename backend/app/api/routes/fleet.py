from fastapi import APIRouter

from mesh.fleet_manager import (
    get_fleet_summary
)

router = APIRouter()

@router.get("/fleet")

def fleet():

    return get_fleet_summary()


