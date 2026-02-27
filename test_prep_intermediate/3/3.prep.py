def rate_limit_summary(logs):
    my_dict = {}
    for log in logs:
        name = log['user']
        status = log['status']
        if status == 429:
            if name not in my_dict:
                my_dict[name] = 0
            my_dict[name] += 1
    return my_dict

print(rate_limit_summary(logs = [
    {"user": "Alice", "status": 200},
    {"user": "Bob", "status": 429},
    {"user": "Alice", "status": 429},
    {"user": "Alice", "status": 200},
    {"user": "Bob", "status": 429},
    {"user": "Charlie", "status": 200},
    {"user": "Bob", "status": 200},
]))


def suspicious_users(logs):
    my_list = []
    my_dict = {}
    for log in logs:
        name = log['user']
        status = log['success']
        if name not in my_dict:
            my_dict[name] = 0
        if status == False:
            my_dict[name] += 1
            if my_dict[name] == 3:
                my_list.append(name)
        else:
            my_dict[name] = 0
            
    return my_list

print(suspicious_users([
    {"user": "Alice", "success": True},
    {"user": "Alice", "success": False},
    {"user": "Alice", "success": False},
    {"user": "Alice", "success": False},
    {"user": "Bob", "success": False},
    {"user": "Bob", "success": True},
    {"user": "Bob", "success": False},
]))


def temperature_peaks(temperatures):
    my_list = []
    for i in range(1, len(temperatures) - 1):
        current = temperatures[i]
        start = temperatures[i - 1]
        end = temperatures[i + 1]
        if current > start and current > end:
            my_list.append(current)
    return my_list

print(temperature_peaks([30, 32, 31, 35, 33, 36, 34, 38, 37, 39, 35]))



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
    {"incident_id": "INC-001", "stage": 1, "duration_hours": 2.5},
    {"incident_id": "INC-002", "stage": 2, "duration_hours": 1.0},
    {"incident_id": "INC-003", "stage": 1, "duration_hours": 3.0},
    {"incident_id": "INC-004", "stage": 2, "duration_hours": 4.0},
]))


def draw_pyramid(height):
    width = 2 * height - 1
    
    my_list = []
    for rows in range(height):
        space = ""
        for cols in range(width):
            if rows == height - 1:
                space += "*"
            elif cols == height - 1 - rows or cols == height - 1 + rows:
                space += "*"
            else:
                space += " "
        my_list.append(space)
    return my_list

# def draw_pyramid(height):
#     pyramid = []
#     for i in range(height):
#         stars = "*" * (2*i + 1)
#         pyramid.append(stars.center(2*height - 1))
#     return pyramid

print(draw_pyramid(4))


def best_sales_streak(sales):
    streaks = {}
    current = {}
    
    for sale in sales:
        employee = sale['employee']
        sold = sale['sold']
        if employee not in streaks:
            streaks[employee] = 0
            current[employee] = 0
        if sold > 0:
            current[employee] += 1
            if current[employee] > streaks[employee]:
                streaks[employee] = current[employee]
        else:
            current[employee] = 0
    return streaks

print(best_sales_streak(sales = [
    {"employee": "Alice", "sold": 3},
    {"employee": "Bob", "sold": 5},
    {"employee": "Alice", "sold": 0},
    {"employee": "Alice", "sold": 4},
    {"employee": "Alice", "sold": 5},
    {"employee": "Bob", "sold": 0},
    {"employee": "Bob", "sold": 2},
    {"employee": "Bob", "sold": 3},
    {"employee": "Bob", "sold": 4},
]))