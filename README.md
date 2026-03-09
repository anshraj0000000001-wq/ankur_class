
# Ankur Classes

**Ankur Classes** is a web platform for online learning with features like:

- Admin panel to manage students, tests, notes, and gallery
- Student panel to access live classes, notes, gallery, and take tests
- JWT authentication for secure login
- Real-time live class chat via WebSocket
- Objective tests with automatic scoring
- Frontend: HTML, CSS, JS (professional dashboard)

---

## 📁 Folder Structure
ankur_classes/ │ ├── backend/ │   ├── main.py │   ├── database.py │   ├── models.py │   ├── auth.py │   └── routes/ │       ├── admin.py │       ├── students.py │       ├── tests.py │       ├── content.py │       └── live_class.py │ ├── frontend/ │   ├── index.html │   ├── admin.html │   ├── student.html │   ├── test.html │   ├── css/ │   │   └── style.css │   └── js/ │       ├── login.js │       ├── admin.js │       ├── student.js │       └── test.js │ ├── requirements.txt └── README.md
Copy code

---

## ⚙️ Installation (Local)

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/ankur_classes.git
cd ankur_classes
Install dependencies:
Bash
Copy code
pip install -r requirements.txt
Run backend server:
Bash
Copy code
uvicorn backend.main:app --reload
Open frontend in browser:
frontend/index.html → Student login
frontend/admin.html → Admin dashboard
🔑 Admin Credentials
Username: ankit__kumar
Password: ankit__2026
Admin can add students, tests, notes, gallery, and manage content.
🧑‍🎓 Student Features
Login with student credentials
Access notes (PDF links) and gallery (images/videos)
Participate in online tests with automatic scoring
Join live class chat
🌐 Deployment (Free Cloud)
Option 1: Render
Push the repo to GitHub.
Create a new Web Service on Render.
Connect GitHub repository.
Build Command:
Bash
Copy code
pip install -r requirements.txt
Start Command:
Bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
Serve frontend via Render Static Site or /static route.
Option 2: Railway
Push repo to GitHub.
Create a new project → Deploy from GitHub.
Railway detects Python automatically.
Start Command:
Bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
Update frontend fetch URLs to Railway backend URL.
🛠️ Notes
JWT secret: ANKUR_CLASSES_SECRET (backend/auth.py)
Database: SQLite (backend/database/ankur.db)
Password hashing: Bcrypt via Passlib
WebSocket: /ws/live-class for real-time live class chat
Use modern browsers for best frontend experience.
📌 Future Enhancements
Add WebRTC video/audio for live classes
Student profile editing
Test timer on frontend
Responsive mobile-friendly design
✅ License
Free to use for educational purposes.
