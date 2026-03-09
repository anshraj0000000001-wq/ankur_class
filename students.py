# backend/routes/students.py

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from routes.auth import create_access_token, verify_password

router = APIRouter()

# ------------------- SCHEMAS -------------------
class StudentLogin(BaseModel):
    username: str
    password: str

# ------------------- DEPENDENCY -------------------
def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- ROUTES -------------------

@router.post("/student/login")
def student_login(data: StudentLogin, db: Session = Depends(get_db)):
    """
    Student login route
    Returns JWT access token, student_id, and name
    """
    student = db.query(models.Student).filter(models.Student.username == data.username).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    if not verify_password(data.password, student.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    token = create_access_token({"sub": student.username})
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "student_id": student.student_id,
        "name": student.name
    }

@router.get("/student/notes")
def get_notes(db: Session = Depends(get_db)):
    """
    Retrieve all notes
    Returns list of notes with title and pdf_link
    """
    notes = db.query(models.Notes).all()
    return [{"id": note.id, "title": note.title, "pdf_link": note.pdf_link} for note in notes]

@router.get("/student/gallery")
def get_gallery(db: Session = Depends(get_db)):
    """
    Retrieve all gallery media
    Returns list of media with media_link and media_type
    """
    media = db.query(models.Gallery).all()
    return [{"id": m.id, "media_link": m.media_link, "media_type": m.media_type} for m in media]