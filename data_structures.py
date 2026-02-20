
# ============================
# TODO:Question 1
# ============================
def split_coords(coordinates: list) -> tuple:
    my_list = []
    new_list = []
    # al = []
    for (x, y) in coordinates:
        my_list.append(x)
        new_list.append(y)
    return (my_list, new_list)

print(split_coords([(12, 45), (15, 48), (18, 51)]))
# ============================
# TODO:Question 2
# ============================
def create_id_lookup(user_data: list) -> dict:
    my_dict = {}
    count = 0
    for data in user_data:
        my_dict.update({data:count})
        count += 1
    return my_dict 
    # return {}
# print(create_id_lookup(["Sipho", "Lerato", "Thandi", "Kobane"]))
# ============================
# TODO:Question 3
# ============================
def extract_unique_tags(posts: list) -> set:
    new_p = []
    for post in posts:
        new_p.append(post.lower())
    
    return set(new_p)

# ============================
# TODO:Question 4
# ============================
def group_by_category(items: list) -> dict:
    grouped = {}

    for item in items:
        name = item["name"]
        category = item["type"]

        if category not in grouped:
            grouped[category] = []

        grouped[category].append(name)

    return grouped

print(group_by_category([{"name": "Boerewors", "type": "Meat"}]))
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
from typing import Union

def batch_api_dispatcher(user_ids: Union[list, tuple]) -> list:
    batch_size = 5
    batches = []
    
    for i in range(0, len(user_ids), batch_size):
        batches.append(list(user_ids[i:i + batch_size]))
    
    return batches


# print(batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7']))

# ============================
# TODO:Question 6
# ============================
def social_graph_inverter(following_list: dict) -> dict:
    followers_dict = {}
    
    for person, follows in following_list.items():
        for followed in follows:
            if followed not in followers_dict:
                followers_dict[followed] = []
            followers_dict[followed].append(person)
    
    return followers_dict

# ============================
# TODO:Question 7
# ============================

def fibonacci_generator(n: int) -> list:
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be non-negative.")

    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    seq = fibonacci_generator(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq


# print(fibonacci_generator(7))
