import random

def dice():
    return str(random.randint(1, 6))

def coin():
    result = random.randint(0, 1)
    if result == 0:
        return "Heads"
    else:
        return "Tails"

def randomize_case(string):
    result = ""
    for char in string:
        if random.choice([True, False]):
            result += char.upper()
        else:
            result += char.lower()
    return result