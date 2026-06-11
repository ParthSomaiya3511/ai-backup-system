from pydantic import BaseModel

class Device(BaseModel):

    device_id: str

    hostname: str

    os: str

    status: str