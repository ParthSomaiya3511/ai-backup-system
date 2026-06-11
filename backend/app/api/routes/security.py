from fastapi import APIRouter

from security.security_center import (
    run_security_scan
)

router = APIRouter()

@router.get("/security/scan")
def scan():

    result = run_security_scan(

        "../../storage/backups"

    )

    return result