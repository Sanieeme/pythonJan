def most_active_user(sessions):
    my_dict = {}
    for session in sessions:
        name = session['user']
        active = session['active']
        if name not in my_dict:
            my_dict(name) = 0
            
        if active == True:
            my_dict[name] += 1
    
    max_user = None
    max_count = -1
    
    for user in my_dict:
        if my_dict[user] > max_count:
            max_count = my_dict[user]
            max_user = user
            
    return max_user