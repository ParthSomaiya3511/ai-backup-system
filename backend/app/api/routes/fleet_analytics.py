from fastapi import APIRouter

from mesh.fleet_analytics import (
    analytics
)

router = APIRouter()

@router.get(
    "/fleet/analytics"
)
def get_analytics():

    return analytics()