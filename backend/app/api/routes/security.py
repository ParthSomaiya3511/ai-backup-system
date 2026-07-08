from fastapi import APIRouter

from app.security.security_center import run_security_scan

router = APIRouter()


@router.get("/security/scan")
def security_scan():

    return run_security_scan()