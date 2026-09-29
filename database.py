import sqlite3
import bcrypt

# Initialize database
def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    # Create users table for authentication (username and hashed password)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)''')

    # Create chat history table
    cursor.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        message TEXT,
                        response TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

# Add a function to register new users
def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # Hash the password
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True  # Successfully registered
    except sqlite3.IntegrityError:
        conn.close()
        return False  # User already exists

# Add a function to authenticate users during login
def authenticate_user(username, password):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cursor.fetchone()  # Fetch stored password
    conn.close()
    
    if stored_password and bcrypt.checkpw(password.encode(), stored_password[0]):
        return True  # Password matches
    else:
        return False  # Invalid credentials

# Function to add chat message and response to chat history
def add_chat(username, message, response):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (username, message, response) VALUES (?, ?, ?)", 
                   (username, message, response))
    conn.commit()
    conn.close()

# Function to retrieve chat history for a user
def get_chat_history(username):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT message, response, timestamp FROM chat_history WHERE username = ?", (username,))
    history = cursor.fetchall()
    conn.close()
    return history

# Function to delete a user
def delete_user(username):
    try:
        # Connect to your database
        conn = sqlite3.connect("chatbot.db")  # Change the path if necessary
        cursor = conn.cursor()

        # Delete user's data from chat history table
        cursor.execute("DELETE FROM chat_history WHERE username = ?", (username,))
        
        # Delete the user from the users table
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))

        # Commit and close the connection
        conn.commit()
        conn.close()
        return True  # Deletion successful
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False  # Deletion failed

# Run this to initialize the database tables
init_db()
