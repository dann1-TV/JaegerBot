import random


def roll():
    return str(random.randint(1, 6))

def coin_flip():
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

def tip(arg):
    
    return "a random tip from the tips array"