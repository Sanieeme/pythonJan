def split_temperatures(readings):
    # your code here
    my_list = []
    other_list = []
    
    for read in readings:
        if read < 20:
            my_list.append(read)
        else:
            other_list.append(read)
    return (my_list, other_list)

print(split_temperatures([18, 22, 19, 25, 17, 20]))

def word_lengths(words):
    my_dict = {}
    count = 0
    for word in words:
        count = len(word)
        
        # for w in word:
        #     count += 1
        my_dict[word] = count
        # count = 0
        
    return my_dict

print(word_lengths(["code", "python", "ai"]))


def get_even_numbers(nums):
    # your code
    my_list = []
    nums = nums[:]
    for num in nums:
        if num % 2 == 0:
            my_list.append(num)
    return set(my_list)

print(get_even_numbers([3, 6, 2, 7, 6, 10, 3]))
        
        
def group_students_by_grade(students):
    # your code
    results = {}
    for student in students:
        cat = student["grade"]
        name = student["name"]
        if cat not in results:
            results[cat] = []
        results[cat].append(name)
        
    return results
            
print(group_students_by_grade([
 {"name": "Lebo", "grade": "A"},
 {"name": "Mia", "grade": "B"},
 {"name": "Sam", "grade": "A"}
]
))