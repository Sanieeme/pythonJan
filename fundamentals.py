# ============================
# TODO:Question 1
# ============================
def pseudo_range(n):
    for i in range(1, n + 1):
        print(i)

# ============================
# TODO:Question 2
# ============================

def do_not_panic(n) -> bool:
    total = 0
    for i in range(1, n + 1):
        total += i        
    return total % 2 == 0     


# ============================
# TODO: Question 3
# ============================

def countdown_even(n: int) -> None:                
    while n >= 0:
        if n % 2 == 0:
            print(n)
        n -= 1 
print(countdown_even(5))
# ============================
# TODO: Question 4
# ============================

def check_password(password: str) -> str:
    if password == "":                    
        return "Invalid"
    elif len(password) < 6:                   
        return "Weak"
    else:
        has_letter = any(True for c in password)
        has_number = any(True for c in password)  
        has_symbol = any(c in '!@#$%^&*' for c in password)  
        
        if has_letter and has_number and has_symbol:      
            return "Strong"
        elif has_letter and has_number:         
            return "Medium"
        else:
            return ""        

# ============================
# TODO: Question 5
# ============================

def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
    # ne = []
    # sen = sentence.strip().split()
    # for s in sen:
    #     rev = s[::-1]
    #     ne.append(rev)
    #     if len(ne) > 2:
    #         reversed_words = " ".join(ne)
    #         return reversed_words
# print(reverse_words("hello world"))
