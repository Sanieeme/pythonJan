🧠 Question 1
📊 Problem: API Rate Limit Monitor

A system logs API calls like this:

logs = [
    {"user": "Alice", "status": 200},
    {"user": "Bob", "status": 429},
    {"user": "Alice", "status": 429},
    {"user": "Alice", "status": 200},
    {"user": "Bob", "status": 429},
    {"user": "Charlie", "status": 200},
    {"user": "Bob", "status": 200},
]
🔹 Task

Write a function:

def rate_limit_summary(logs):

That returns a dictionary showing how many times each user received a 429 (rate limit) error.

✅ Expected Output
{
    "Alice": 1,
    "Bob": 2
}



🧠 Question 2 — Suspicious Login Detector

You are given a list of login attempts:

logs = [
    {"user": "Alice", "success": True},
    {"user": "Alice", "success": False},
    {"user": "Alice", "success": False},
    {"user": "Alice", "success": False},
    {"user": "Bob", "success": False},
    {"user": "Bob", "success": True},
    {"user": "Bob", "success": False},
]
🔎 Task

Write a function:

def suspicious_users(logs):

Return a list of users who had 3 consecutive failed logins.

✅ Expected Output
["Alice"]



🧠 Question 3 — Temperature Peaks

You are given a list of daily temperatures:

temperatures = [30, 32, 31, 35, 33, 36, 34, 38, 37, 39, 35]
🔹 Task

Write a function:

def temperature_peaks(temperatures):

It should return a list of all temperatures that are higher than both their neighbors.

A temperature is a "peak" if it is strictly greater than the previous and next day.

Ignore the first and last day (they don’t have two neighbors).

✅ Example
temperature_peaks([30, 32, 31, 35, 33, 36, 34, 38, 37, 39, 35])
# Output: [32, 35, 36, 38, 39]



🧠 Question 4 — Stage Duration Summary

You are given a list of incident records. Each record contains a “stage” and a “duration”:

records = [
    {"incident_id": "INC-001", "stage": 1, "duration_hours": 2.5},
    {"incident_id": "INC-002", "stage": 2, "duration_hours": 1.0},
    {"incident_id": "INC-003", "stage": 1, "duration_hours": 3.0},
    {"incident_id": "INC-004", "stage": 2, "duration_hours": 4.0},
]
🔹 Task

Write a function:

def stage_summary(records):

It should return a dictionary that sums the total duration per stage.

✅ Example Output
{
    "Stage 1": 5.5,
    "Stage 2": 5.0
}


🧠 Question 5 — Pyramid Drawer

Write a function:

def draw_pyramid(height):

It should return a list of strings that visually represents a pyramid of the given height using *.

🔹 Rules

Each row has stars centered.

The pyramid should have height rows.

The base row should have (2 * height - 1) stars.

Return a list of strings, one string per row.

🔹 Example
draw_pyramid(4)

Expected output:

[
   "   *   ",
   "  ***  ",
   " ***** ",
   "*******"
]


🧠 Final Challenge — Sales Streak Analyzer

You are given a list of daily sales per employee:

sales = [
    {"employee": "Alice", "sold": 3},
    {"employee": "Bob", "sold": 5},
    {"employee": "Alice", "sold": 0},
    {"employee": "Alice", "sold": 4},
    {"employee": "Alice", "sold": 5},
    {"employee": "Bob", "sold": 0},
    {"employee": "Bob", "sold": 2},
    {"employee": "Bob", "sold": 3},
    {"employee": "Bob", "sold": 4},
]
🔹 Task

Write a function:

def best_sales_streak(sales):

It should return a dictionary showing the longest consecutive days of non-zero sales for each employee.

🔹 Example Output
{
    "Alice": 3,  # 4 → 5 → 5 consecutive non-zero sales
    "Bob": 3     # 2 → 3 → 4 consecutive non-zero sales
}