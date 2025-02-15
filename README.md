📜 README.md (Professional & Beginner-Friendly)

# 🏆 Legal Tech Trainer - Backend Dashboard

This is a **backend dashboard application** built with **FastAPI and SQLite**.  
It includes **user progress tracking, point assignment for tasks, milestone achievements, and a real-time dashboard API**.

---

## 🚀 **Installation**

### **1️⃣ Clone the Repository**
```sh
git clone git@github.com:Psychic/legal-tech-game.git
cd legal-tech-game
2️⃣ Set Up a Virtual Environment
🔹 Mac & Linux

python3 -m venv venv
source venv/bin/activate
🔹 Windows

python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🏃 Running the Application

1️⃣ Start the Backend Server
cd backend
uvicorn main:app --reload
✅ The server will run on http://127.0.0.1:8000
✅ Open http://127.0.0.1:8000/docs to see API documentation.

2️⃣ Start the Frontend (Trainer Game)
cd static
python3 -m http.server 8001
✅ Open http://127.0.0.1:8001/trainer.html in your browser.

📡 API Routes

🔐 User Authentication Routes

Method	Route	Description
POST	/api/auth/signup	Registers a new user
POST	/api/auth/login	Logs in a user
🔹 POST /api/auth/signup
Registers a new user.
✅ Request Body:

{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "securepassword"
}
✅ Response:

{
  "message": "User registered successfully"
}
🔹 POST /api/auth/login
Logs in a user.
✅ Request Body:

{
  "email": "johndoe@example.com",
  "password": "securepassword"
}
✅ Response:

{
  "token": "JWT_TOKEN",
  "userId": "string",
  "name": "John Doe",
  "email": "johndoe@example.com"
}
🎯 Point System Routes

Method	Route	Description
POST	/api/points/update	Assigns points for task completion
🔹 POST /api/points/update
✅ Request Body:

{
  "user_id": "user123",
  "activity": "quiz"
}
✅ Response:

{
  "message": "Points updated successfully",
  "added_points": 50
}
🏆 Milestone Routes

Method	Route	Description
POST	/api/milestone/achieve	Handles bonus points for milestone achievements
🔹 POST /api/milestone/achieve
✅ Request Body:

{
  "user_id": "user123",
  "milestone": "Completed NDA Automation",
  "reward_points": 100
}
✅ Response:

{
  "message": "Milestone achieved!",
  "totalPoints": 200
}
📊 Dashboard Routes

Method	Route	Description
GET	/api/dashboard/summary?user_id=user123	Gets a summary of the user's dashboard
GET	/api/dashboard/details?user_id=user123	Gets detailed user progress
🔹 GET /api/dashboard/summary?user_id=user123
✅ Response:

{
  "name": "John Doe",
  "total_points": 150,
  "progress": {
    "quiz_completed": 2,
    "nda_completed": 1,
    "workflow_completed": 0
  }
}
🔹 GET /api/dashboard/details?user_id=user123
✅ Response:

{
  "name": "John Doe",
  "total_points": 150,
  "activities": [
    { "name": "Quiz 1", "points": 50, "completed": true },
    { "name": "NDA Automation", "points": 75, "completed": true }
  ],
  "milestones": [
    { "name": "Beginner Badge", "rewardPoints": 25, "achieved": true }
  ]
}
🔥 Common Issues & Fixes

❌ 1. ModuleNotFoundError: No module named 'fastapi'
✅ Fix:

source venv/bin/activate
pip install -r requirements.txt
❌ 2. uvicorn: command not found
✅ Fix:

pip install uvicorn
❌ 3. git@github.com: Permission denied (publickey)
✅ Fix:

ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
cat ~/.ssh/id_rsa.pub  # Add this key to GitHub under SSH Keys
📜 Database Schema

This project uses SQLite to store user progress.

User Model
{
  "user_id": "string",
  "name": "string",
  "email": "string",
  "password": "hashed_string",
  "total_points": 0,
  "activities": [
    {
      "name": "Quiz 1",
      "points": 50,
      "completed": true,
      "dateCompleted": "2024-02-13T12:00:00Z"
    }
  ],
  "milestones": [
    {
      "name": "Beginner Badge",
      "rewardPoints": 25,
      "achieved": true,
      "dateAchieved": "2024-02-13T12:00:00Z"
    }
  ]
}
👨‍💻 Contributing

Feel free to submit issues or pull requests! Contributions are welcome.

⚖️ License

This project is open-source and free to use.


---

## **📌 How to Use This README**
1. **Save this file as `README.md`** inside your **project folder (`legal-tech-game/`)**.  
2. **Commit & push it to GitHub**:
   ```sh
   git add README.md
   git commit -m "Added README with installation instructions"
   git push origin main
Now, anyone can follow these steps to install & run your project! 🚀
