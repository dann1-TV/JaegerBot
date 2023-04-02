import random

def random_tip(tips):
    return random.choice(tips)

def random_map(maps):
    return random.choice(maps)

def load_data():
    data = {}
    data['maps'] = load_conf("maps.txt")
    data['tips'] = load_conf("tips.txt")

    return data

# returns array of lines loaded from file
def load_conf(file_path):
    lines = []

    with open(file_path, 'r') as file:
        content = file.read()
        lines = content.split("\n")

    return lines