🧠 Mini Test – Question 1
📊 Active User Analyzer

You are given a list of session logs:

sessions = [
    {"user": "Alice", "active": True},
    {"user": "Bob", "active": False},
    {"user": "Alice", "active": True},
    {"user": "Alice", "active": False},
    {"user": "Bob", "active": True},
    {"user": "Bob", "active": True},
    {"user": "Charlie", "active": False},
]
🔹 Task

Write a function:

def most_active_user(sessions):

Return the name of the user with the highest number of active=True sessions.

⚠️ Rules

Count only when active == True

If two users tie, return any one of them

Assume the list is not empty

Do not use collections.Counter (use loops + dictionary)

✅ Expected Result for Above Data
"Alice"