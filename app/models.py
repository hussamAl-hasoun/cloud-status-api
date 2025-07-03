from sqlalchemy import Column, String
from app.database import Base

class CloudService(Base):
    __tablename__ = "cloud_services"

    name = Column(String, primary_key=True, index=True)
    status = Column(String)

from pydantic import BaseModel
# قاعدة البيانات ORM model

# API Response model
class ServiceStatus(BaseModel):
    name: str
    status: str
from app.models import ServiceStatus