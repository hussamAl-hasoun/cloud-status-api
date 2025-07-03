from sqlalchemy.orm import Session
from app.models import CloudService

def get_all_statuses(db: Session):
    return db.query(CloudService).all()

def update_status(db: Session, service_name: str, new_status: str):
    service = db.query(CloudService).filter(CloudService.name == service_name).first()
    if not service:
        return None
    service.status = new_status
    db.commit()
    db.refresh(service)
    return service
