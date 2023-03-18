#!/usr/bin/env python

import tarkov
import bot_basic

data = tarkov.load_data()

print(tarkov.random_map(data['maps']))
print(tarkov.random_tip(data['tips']))