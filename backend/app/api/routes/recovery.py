from fastapi import APIRouter

router = APIRouter()

@router.get("/recovery")
def get_recovery():

    return {

        "recoverable_files": 50

    }