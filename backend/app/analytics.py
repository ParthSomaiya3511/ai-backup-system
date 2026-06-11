from fastapi import APIRouter

from analytics import dashboard_stats

router = APIRouter()

@router.get("/analytics")

def analytics():

    return dashboard_stats()