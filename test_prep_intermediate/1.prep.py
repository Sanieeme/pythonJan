from typing import Union
# ============================
# TODO:Question 1
# ============================
def split_coords(coordinates: list) -> tuple:
    list1 = []
    list2 = []
    for c, d in coordinates:
        list1.append(c)
        list2.append(d)
    return (list1, list2)

# print(split_coords([(12, 45), (15, 48), (18, 51)]))
# ============================
# TODO:Question 2
# ============================
def create_id_lookup(user_data: list) -> dict:
    count = 0
    my_dict = {}
    for data in user_data:
        count += 1
        my_dict[data] = count
    return my_dict
    
# print(create_id_lookup(["Sipho", "Lerato", "Thandi", "Kobane"]))
# ============================
# TODO:Question 3
# ============================
def extract_unique_tags(posts: list) -> set:
    my = []
    for post in posts:
        my.append(post.lower())
    return set(my)

# print(extract_unique_tags(['Python', 'python', 'JAVA', 'Data', 'data', 'DATA', 'Code']))

# ============================
# TODO:Question 4
# ============================
def group_by_category(items: list) -> dict:
    new_dict = {}
    for item in items:
        if item['type'] in new_dict:
            new_dict[item['type']].append(item['name'])
        else:
            new_dict[item['type']] = [item['name']]
            
    return new_dict
# print(group_by_category([{"name": "Boerewors", "type": "Meat"}]))
# print(group_by_category([{"name": "Boerewors", "type": "Meat"},
#                          {"name": "Charcoal", "type": "Hardware"},
#                          {"name": "Lamb Chops", "type": "Meat"},
#                          {"name": "Chakalaka", "type": "Canned Goods"}
#                          ]
#                          )
#                          )
# ============================
# TODO:Question 5
# ============================

def batch_api_dispatcher(user_ids: Union[list, tuple])-> tuple:
    list1 = []
    result = ()
    for id in user_ids:
        list1.append(id)
        if len(list1) == 5:
            result += (list1, )
            list1 = []
    if list1:
        result += (list1, )
    return result

print(batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7']))
# ============================
# TODO:Question 6
# ============================
def social_graph_inverter(following_list: dict) -> dict:
    my_dict = {}
    for key, value in following_list.items():
        for v in value:
            if v in my_dict:
                my_dict[v].append(key)
            else:
                my_dict[v] = [key]

    return my_dict

print(social_graph_inverter({"Alice": ["Bob", "Charlie"], "Bob": ["Charlie"]}))

# ============================
# TODO:Question 7
# ============================
# print(fib(7))
def fibonacci_generator(n: int) -> list:
    ...
    my_dict = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        for i in range(2, n):
            nums = my_dict[i - 1] + my_dict[i - 2]
            my_dict.append(nums)
    return my_dict
# print(fibonacci_generator(7))


def invert_enrollment(data: dict) -> dict:
    my_dict = {}
    for key, value in data.items():
        for v in value:
            if v in my_dict:
                my_dict[v].append(key)
            else:
                my_dict[v] = [key]
    return my_dict

# print(invert_enrollment({
#     "Math": ["Alice", "Charlie"],
#     "Physics": ["Alice", "Bob"],
#     "Chemistry": ["Bob"]
# }
# ))

def group_by_skill(data: dict) -> dict:
    my_dict = {}
    for key, value in data.items():
        for v in value:
            if v in my_dict:
                my_dict[v].append(key)
            else:
                my_dict[v] = [key]
    return my_dict

# print(group_by_skill({
#     "Python": ["Alice", "Bob"],
#     "SQL": ["Alice", "Charlie"],
#     "Java": ["Bob"],
#     "C++": ["Charlie"]
# }
# ))

def club_popularity(data: dict) -> list:
    club_count = {}
    
    # Step 1: Count members per club
    for student, clubs in data.items():
        for club in clubs:
            if club in club_count:
                club_count[club] += 1
            else:
                club_count[club] = 1
    
    # Step 2: Convert to list of tuples
    result = list(club_count.items())
    
    # Step 3: Sort
    # result.sort(key=lambda x: (-x[1], x[0]))
    
    return result

print(club_popularity({
    "Alice": ["Chess", "Robotics"],
    "Bob": ["Chess"],
    "Charlie": ["Robotics", "Drama"],
    "David": ["Chess", "Drama"]
}
))

def analyze_logs(logs: list) -> list:
    data = {}
    for log in logs:
        level, user, action = log.split(":")
        
        if level in data:
            data[level]['count'] += 1
            data[user]['users'].add(user)
    result = []
    
    for level in data:
        count = data[level]['count']
        users = sorted(data[level]['users'])
        user_string = ",".join(users)
    result.append((level, count, user_string))
        
    output = []
    for level, count, users in result:
        o = f"{level} - {count} - Users: {users}"
        output.append(f"{level} - {count} - Users: {users}")
            
    return output

print(analyze_logs(logs = [
    "INFO:User1:Login",
    "ERROR:User2:PaymentFailed",
    "INFO:User1:Upload",
    "WARNING:User3:PasswordWeak",
    "ERROR:User2:Timeout",
    "INFO:User2:Login",
    "ERROR:User1:Crash"
]

))