import random

def random_tip(tips):
    return random.choice(tips)

def random_map(maps):
    return random.choice(maps)

def load_tips():
    return load_conf("tips.txt")

def load_maps():
    return load_conf("maps.txt")
    
# returns array of lines loaded from file
def load_conf(conf_file_name):
    
    with open(conf_file_name, 'r') as file:
        content = file.read()
        content = content.split("\n")

    return content
