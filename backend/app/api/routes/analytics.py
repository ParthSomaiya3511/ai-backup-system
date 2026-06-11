from fastapi import APIRouter

from security.security_analytics import analytics

router = APIRouter()

@router.get("/security/analytics")

def get_analytics():

    return analytics()