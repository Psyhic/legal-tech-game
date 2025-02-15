from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import database

# Initialize database
database.init_db()

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request structure
class ActivityUpdate(BaseModel):
    user_id: str
    activity: str  # quiz, nda, workflow, certification

# Points allocation
POINTS = {
    "quiz": 50,
    "nda": 75,
    "workflow": 75,
    "certification": 50
}

@app.post("/api/points/update")
def update_points(data: ActivityUpdate):
    """API to update user points based on activity."""
    if data.activity not in POINTS:
        raise HTTPException(status_code=400, detail="Invalid activity type")

    database.update_points(data.user_id, data.activity, POINTS[data.activity])
    
    return {"message": "Points updated successfully", "added_points": POINTS[data.activity]}

@app.get("/api/dashboard/summary")
def get_dashboard_summary(user_id: str):
    """API to fetch user progress summary."""
    user_data = database.get_user_progress(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user_data
