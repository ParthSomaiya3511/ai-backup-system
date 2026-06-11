from fastapi import APIRouter

router = APIRouter()

users = []

@router.post("/users")

def create_user(user: dict):

    users.append(user)

    return {

        "success": True

    }
    
    
@router.get("/users")

def get_users():

    return users


@router.delete("/users/{user_id}")

def delete_user(user_id:int):

    return {

        "deleted": user_id

    }