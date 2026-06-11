from fastapi import APIRouter

from auth.models import LoginRequest

from auth.service import login_user

router = APIRouter()


@router.post("/login")
def login(data: LoginRequest):

    return login_user(
        data.email,
        data.password
    )