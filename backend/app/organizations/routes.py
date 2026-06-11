from fastapi import APIRouter

router = APIRouter()

organizations = []


@router.post("/organizations")

def create_org(org:dict):

    organizations.append(org)

    return {

        "success": True

    }
    
    
@router.get("/organizations")

def get_orgs():

    return organizations