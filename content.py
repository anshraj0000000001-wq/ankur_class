from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

# ------------------- SCHEMAS -------------------
class NoteCreate(BaseModel):
    title: str
    pdf_link: str

class GalleryCreate(BaseModel):
    media_link: str
    media_type: str  # 'image' or 'video'

# ------------------- DEPENDENCY -------------------
def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- ROUTES -------------------
@router.post("/admin/add-note")
def add_note(data: NoteCreate, db: Session = Depends(get_db)):
    """Add a note (PDF link) to the database"""
    note = models.Notes(title=data.title, pdf_link=data.pdf_link)
    db.add(note)
    db.commit()
    db.refresh(note)
    return {"message": "Note added", "note_id": note.id}

@router.post("/admin/add-gallery")
def add_gallery(data: GalleryCreate, db: Session = Depends(get_db)):
    """Add media (image/video) to the gallery"""
    media = models.Gallery(media_link=data.media_link, media_type=data.media_type)
    db.add(media)
    db.commit()
    db.refresh(media)
    return {"message": "Media added", "media_id": media.id}