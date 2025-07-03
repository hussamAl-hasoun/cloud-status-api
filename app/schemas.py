from pydantic import BaseModel

class ServiceStatus(BaseModel):
    name: str
    status: str

    class Config:
        orm_mode = True
