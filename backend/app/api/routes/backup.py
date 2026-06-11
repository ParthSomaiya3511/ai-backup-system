from fastapi import APIRouter

router = APIRouter()

@router.get("/backups")
def get_backups():

    return {

        "success": True,

        "total_backups": 120

    }