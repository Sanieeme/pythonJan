def total_spent_per_customer(orders: list) -> dict:
    my_dict = {}
    for order in orders:
        amount = order['amount']
        customer = order['customer']
        
        if customer not in my_dict:
            my_dict[customer] = 0
        my_dict[customer] += amount
    return my_dict

print(total_spent_per_customer(orders = [
    {"id": 1, "customer": "Sipho", "amount": 250},
    {"id": 2, "customer": "Lerato", "amount": 400},
    {"id": 3, "customer": "Sipho", "amount": 150},
]))


def login_summary(attempts: list) -> dict:
    my_dict = {}
    for username, success in attempts:
        if username not in my_dict:
            my_dict[username] = {'success': 0, 'fail': 0}
        if success:
            my_dict[username]['success'] += 1
        else:
            my_dict[username]['fail'] += 1
    return my_dict

print(login_summary(attempts = [
    ("Sipho", True),
    ("Lerato", False),
    ("Sipho", False),
    ("Thandi", True),
]))

# return {
#     "Sipho": {"success": 1, "fail": 1},
#     "Lerato": {"success": 0, "fail": 1},
#     "Thandi": {"success": 1, "fail": 0}
# }


def most_followed_user(following: dict) -> str:
    followers_count = {}
    count = 0
    for follower, follow_list in following.items():
        for followed_user in follow_list:
            if followed_user not in followers_count:
                followers_count[followed_user] = 0
            followers_count[followed_user]
    if not followers_count:
        return None
    max_user = None
    max_count = -1
    for user, count in followers_count.items():
        if count > max_count:
            max_user = count
            max_user = user
    return max_user


print(most_followed_user(following = {
    "Sipho": ["Lerato", "Thandi"],
    "Lerato": ["Thandi"],
    "Thandi": []
}))