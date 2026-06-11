from pydantic import BaseModel

class Organization(BaseModel):

    name: str

    plan: str

    users: int

    devices: int