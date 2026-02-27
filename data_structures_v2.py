
# ============================
# TODO:Question 1
# ============================


def pair_coordinates(x_vals: list[int], y_vals: list[int]) -> list[tuple[int, int]]:
    my_list = []

    for x, y in list(zip(x_vals, y_vals)):
        my_list.append((x, y))
    return my_list

# print(pair_coordinates([12, 15, 18], [45, 48, 51]))
# ============================
# TODO:Question 2
# ============================

def count_occurrences(items: list[str]) -> dict[str, int]:
    my_dict = {}
    count = 0
    for item in set(items):     
        my_dict.update({item: items.count(item)})
    return my_dict

# print(count_occurrences(["Bafana", "Soccer", "Bafana", "Goals", "Soccer", "Bafana"]))
# ============================
# TODO:Question 3
# ============================

def find_common_skills(applicants: dict[str, list[str]]) -> set[str]:
    common_skills = None
    
    for skills in applicants.values():
        if common_skills is None:
            common_skills = set(skills)
        else:
            new_common = set()
            for skill in common_skills:
                if skill in skills:
                    new_common.add(skill)
            common_skills = new_common
    
    return common_skills

print(find_common_skills({
    "Lerato": ["Python", "SQL", "Git", "Docker"],
    "Thabo":  ["Python", "SQL", "Java", "Git"],
    "Nandi":  ["Python", "SQL", "Git", "React"]
}))

# ============================
# TODO:Question 4
# ============================

def flatten_schedule(schedule: list[list[str]]) -> list[str]:
    my_list = []
    for module in schedule:
        if module == []:
            return []
        if isinstance(module, list):
            my_list.extend(module)
        else:
            my_list.append(module)
    return my_list

# print(flatten_schedule([["Maths", "English"], ["Science", "History"], ["Art", "PE", "Coding"]]))
# ============================
# TODO:Question 5
# ============================

def sliding_window_sum(numbers: list[int], window_size: int) -> list[int]:
    result = []
    
    # Loop until the last possible window
    for i in range(len(numbers) - window_size + 1):
        window_sum = 0
        
        # Sum the next k elements
        for j in range(window_size):
            window_sum += numbers[i + j]
        
        result.append(window_sum)
    
    return result

print(sliding_window_sum([2, 4, 6, 8, 10], 3))
# ============================
# TODO:Question 6
# ============================

def group_by_province(cities: list[dict[str, str]]) -> dict[str, list[str]]:
    my_dict = {}
    for city in cities:
        city_name = city['city']
        pro_name = city['province']
        if pro_name not in my_dict:
            my_dict[pro_name] = []
        my_dict[pro_name] += [city_name]
    return my_dict

# print(group_by_province([
#     {"city": "Durban",           "province": "KwaZulu-Natal"},
#     {"city": "Pietermaritzburg", "province": "KwaZulu-Natal"},
#     {"city": "Bloemfontein",    "province": "Free State"},
#     {"city": "Welkom",          "province": "Free State"},
#     {"city": "Polokwane",       "province": "Limpopo"}
# ]))
