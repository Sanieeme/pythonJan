
import re

def inventory_audit(stock_totals):
    return sum(stock_totals)

def black_friday(prices_list):
    black = []
    num = 0
    for price in prices_list:
        num = price * (50 / 100)
        black.append(f"R {int(num)}")
    return black

def retry_pin(pin):
    while True:
        num = input("Enter your PIN:")
        if pin == num and len(num) == 4:
            print("Acces Granted!")
            break
        else:
            print("Incorrect PIN. Try again.")

def winning_streak(streak):
    w = ""
    for s in streak:
        w += s
    st = w.split("L")

    return len(max(st))

def peak_finder(temperatures):
    my_list = []
    
    for i in range(1, len(temperatures) - 1):
        left = temperatures[i - 1]
        right = temperatures[i + 1]
        current = temperatures[i]
        if current > left and current > right:
            my_list.append(current)

    return my_list
        
print(peak_finder([5, 10, 5, 10, 5, 10, 5]))

def uuid_validator(list_of_uuids):
    result = {
        "valid_uuids": [],
        "invalid_uuids": []
    }

    hex_chars = "0123456789abcdef"

    for uuid in list_of_uuids:
        is_valid = True

        if len(uuid) != 36:
            is_valid = False

        elif uuid[8] != "-" or uuid[13] != "-" or uuid[18] != "-" or uuid[23] != "-":
            is_valid = False

        else:
            for i in range(len(uuid)):
                if i in [8, 13, 18, 23]:
                    continue
                if uuid[i].lower() not in hex_chars:
                    is_valid = False
                    break

        if is_valid:
            result["valid_uuids"].append(uuid)
        else:
            result["invalid_uuids"].append(uuid)

    return result


print(uuid_validator(["550e8400-e29b-41d4-a716-446655440000", "abc-123-gh-789"]))

def inventory_depletion(inventory, daily_sales_projections):

    if inventory == 0:
        return "Inventory depleted."

    stock = inventory

    for day in range(len(daily_sales_projections)):
        stock -= daily_sales_projections[day]

        if stock < 0:
            return f"Inventory will run out on day {day + 1}."

    return f"Inventory will last through the entire projection period. Remaining stock: {stock}"

