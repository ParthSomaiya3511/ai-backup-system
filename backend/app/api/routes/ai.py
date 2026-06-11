from fastapi import APIRouter

router = APIRouter()

@router.get("/ai")
def get_ai():

    return {

        "important_files": 500,

        "duplicates": 15,

        "threats": 0

    }