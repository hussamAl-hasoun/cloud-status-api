from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os

from app.database import Base, engine, SessionLocal
from app.models import CloudService
from app.schemas import ServiceStatus
from app.services import get_all_statuses, update_status

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud Status API")

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

class StatusUpdate(BaseModel):
    status: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    services = get_all_statuses(db)
    return templates.TemplateResponse("index.html", {"request": request, "services": services})

@app.get("/status", response_model=list[ServiceStatus])
def read_statuses(db: Session = Depends(get_db)):
    return get_all_statuses(db)

@app.post("/status/{service_name}", response_model=ServiceStatus)
def update_service_status(service_name: str, update: StatusUpdate, db: Session = Depends(get_db)):
    result = update_status(db, service_name, update.status)
    if not result:
        raise HTTPException(status_code=404, detail="Service not found")
    return result

# إدخال بيانات مبدئية إذا كانت القاعدة فارغة
from app.models import CloudService

with SessionLocal() as db:
    if not db.query(CloudService).first():
        db.add_all([
            CloudService(name="AWS EC2", status="operational"),
            CloudService(name="Azure Storage", status="degraded performance"),
            CloudService(name="GCP Compute", status="major outage"),
        ])
        db.commit()
