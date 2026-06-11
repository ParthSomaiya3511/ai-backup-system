from fastapi import APIRouter

from security.report_generator import generate_report

router = APIRouter()

@router.get("/security/report")

def report():

    return generate_report()