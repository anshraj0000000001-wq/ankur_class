from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import random
from passlib.context import CryptContext

router = APIRouter()

# ------------------- CONFIG -------------------
ADMIN_USERNAME = "ankit__kumar"
ADMIN_PASSWORD = "ankit__2026"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ------------------- SCHEMAS -------------------
class AdminLogin(BaseModel):
    username: str
    password: str

class StudentCreate(BaseModel):
    name: str
    username: str
    password: str

# ------------------- HELPER FUNCTIONS -------------------
def generate_student_id():
    """Generate unique student ID"""
    number = random.randint(1000, 9999)
    return f"ANKUR{number}"

# ------------------- ROUTES -------------------
@router.post("/admin/login")
def admin_login(data: AdminLogin):
    """Admin login route"""
    if data.username == ADMIN_USERNAME and data.password == ADMIN_PASSWORD:
        return {"message": "Admin Login Successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/admin/add-student")
def add_student(student: StudentCreate):
    """Add new student with hashed password"""
    db: Session = SessionLocal()
    
    # Check if username already exists
    existing = db.query(models.Student).filter(models.Student.username == student.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Generate student ID
    student_id = generate_student_id()

    # Hash password
    hashed_password = pwd_context.hash(student.password)

    # Create student object
    new_student = models.Student(
        name=student.name,
        username=student.username,
        password=hashed_password,
        student_id=student_id
    )

    # Save to database
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()

    return {
        "message": "Student added successfully",
        "student_id": student_id
    }