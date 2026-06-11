from fastapi import APIRouter

router = APIRouter()

@router.get("/incidents")
def get_incidents():

    return [

        {
            "id": 1,
            "type": "Malware",
            "severity": "HIGH"
        },

        {
            "id": 2,
            "type": "Ransomware",
            "severity": "CRITICAL"
        }

    ]