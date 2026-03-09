# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models

# Routers
from routes import admin
from routes import students
from routes import tests
from routes import content
from routes import live_class

# ------------------- DATABASE -------------------
models.Base.metadata.create_all(bind=engine)

# ------------------- FASTAPI APP -------------------
app = FastAPI(
    title="Ankur Classes API",
    description="Backend API for Ankur Classes - student login, admin panel, tests, notes, gallery, live class",
    version="1.0.0"
)

# ------------------- CORS SETUP -------------------
origins = [
    "https://ankurclasses.netlify.app",  # Netlify frontend URL
    #"http://localhost:5500"                # Local testing URL (Live Server)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- ROUTERS -------------------
app.include_router(admin.router)
app.include_router(students.router)
app.include_router(tests.router)
app.include_router(content.router)
app.include_router(live_class.router)

# ------------------- ROOT -------------------
@app.get("/")
def home():
    return {"message": "Welcome to Ankur Classes API"}