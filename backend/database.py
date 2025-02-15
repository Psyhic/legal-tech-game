import sqlite3

DB_FILE = "points.db"

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_points (
        user_id TEXT PRIMARY KEY,
        total_points INTEGER DEFAULT 0,
        quiz_completed INTEGER DEFAULT 0,
        nda_completed INTEGER DEFAULT 0,
        workflow_completed INTEGER DEFAULT 0,
        certifications_unlocked INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def update_points(user_id, activity, points):
    """Update user points in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_points WHERE user_id=?", (user_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO user_points (user_id) VALUES (?)", (user_id,))

    cursor.execute(f"""
        UPDATE user_points
        SET {activity}_completed = {activity}_completed + 1,
            total_points = total_points + ?
        WHERE user_id = ?
    """, (points, user_id))

    conn.commit()
    conn.close()

def get_user_progress(user_id):
    """Retrieve user progress from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT total_points, quiz_completed, nda_completed, workflow_completed, certifications_unlocked FROM user_points WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    
    conn.close()
    
    if not user:
        return None
    
    return {
        "total_points": user[0],
        "progress": {
            "quiz_completed": user[1],
            "nda_completed": user[2],
            "workflow_completed": user[3],
            "certifications_unlocked": user[4]
        }
    }
