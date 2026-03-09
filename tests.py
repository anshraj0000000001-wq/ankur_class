from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

# ------------------- SCHEMAS -------------------
class TestCreate(BaseModel):
    title: str
    duration: int  # in minutes

class QuestionCreate(BaseModel):
    test_id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str  # 'A', 'B', 'C', 'D'

class SubmitTest(BaseModel):
    student_id: str
    test_id: int
    answers: dict  # {question_id: 'A/B/C/D'}

# ------------------- DEPENDENCY -------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- ROUTES -------------------
@router.post("/admin/create-test")
def create_test(data: TestCreate, db: Session = Depends(get_db)):
    """Admin creates a new test"""
    new_test = models.Test(title=data.title, duration=data.duration)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return {"message": "Test created", "test_id": new_test.id}

@router.post("/admin/add-question")
def add_question(data: QuestionCreate, db: Session = Depends(get_db)):
    """Admin adds a question to a test"""
    # Optional: check if test exists
    test = db.query(models.Test).filter(models.Test.id == data.test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")

    question = models.Question(
        test_id=data.test_id,
        question=data.question,
        option_a=data.option_a,
        option_b=data.option_b,
        option_c=data.option_c,
        option_d=data.option_d,
        correct_answer=data.correct_answer
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return {"message": "Question added", "question_id": question.id}

@router.post("/student/submit-test")
def submit_test(data: SubmitTest, db: Session = Depends(get_db)):
    """Student submits answers for a test"""
    questions = db.query(models.Question).filter(models.Question.test_id == data.test_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="Test not found")

    score = 0
    for q in questions:
        ans = data.answers.get(str(q.id))
        if ans and ans.upper() == q.correct_answer.upper():
            score += 1

    result = models.Result(
        student_id=data.student_id,
        test_id=data.test_id,
        marks=score
    )
    db.add(result)
    db.commit()
    db.refresh(result)

    return {"message": "Test submitted", "marks": score}