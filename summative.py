##################
#   Question 1   #
##################
from typing import Union
def batch_api_dispatcher(user_ids: Union[list, tuple]) -> list:
    batch = 5
    my_list = []
    new_list = []
    for id in user_ids:
        my_list.append(id)
        if len(my_list) == batch:
            new_list.append(my_list)
            my_list = []
    if my_list:
        new_list.append(my_list)
    return new_list

print(batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7']))

##################
#   Question 2   #
##################

def winning_streak(streak):
    new_str = ""
    for s in streak:
        new_str += s
    new_streak = new_str.split('L')
    # print(new_streak)

    return (len(max(new_streak)))

# winning_streak(["W", "L", "W", "W", "L", "W", "W", "W"])
##################
#   Question 3   #
##################

def peak_finder(temperatures):
    my_list = []
    for i in range(1, len(temperatures) - 1):
        current = temperatures[i]
        left = temperatures[i - 1]
        right = temperatures[i + 1]
        if current > left and current > right:
            my_list.append(current)

    return my_list

print(peak_finder([30, 32, 31, 35, 33, 36, 34, 38, 37, 39, 35, 40, 38, 37, 36, 35, 34, 33, 32, 31, 30]))

##################
#   Question 4   #
##################
def stage_summary(records):
    my_dict = {}
    for record in records:
        stage = f"Stage {record['stage']}"
        duration = record['duration_hours']
        if stage not in my_dict:
            my_dict[stage] = 0
        my_dict[stage] += duration
        
    for key in my_dict:
        my_dict[key] = round(my_dict[key], 2)
    return my_dict

print(stage_summary([
    {"incident_id": "ESK-20240601-001", "area": "Soweto", "municipality": "City of Johannesburg", "province": "Gauteng", "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00", "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200},
    {"incident_id": "ESK-20240601-002", "area": "Sandton", "municipality": "City of Johannesburg", "province": "Gauteng", "stage": 4, "duration_hours": 4.0, "date": "2024-06-01", "start_time": "08:00", "end_time": "12:00", "status": "resolved", "scheduled": True, "affected_customers": 8750}
]))
##################
#   Question 5   #
##################

def draw_triangle(height):
    triangle = []
    width = 2 * height - 1
    
    if height == 1:
        return ['*']
    
    for row in range(height):
        line = ""
        for col in range(width):
            if row == height - 1:
                line += "*"
            elif col == height - 1 - row or col == height - 1 + row:
                line += "*"
            else:
                line += " "
        triangle.append(line.rstrip())
    return triangle

print(draw_triangle(5))
