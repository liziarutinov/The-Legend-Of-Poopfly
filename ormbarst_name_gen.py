# import sys
# import time
import random
from random import randint

# def zzz (text, väntan=0.05):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(väntan)
#     print()

def von_ormbarst_namn():
    antal = randint(1, 2)
    repeat = antal
    name = ""
    for i in range(repeat):
        if i == 0:
            konsonant = random.choice("bcdfghjklmnpqrstvwxz").upper()
        else:
            konsonant = random.choice("bcdfghjklmnpqrstvwxz")
        vokal = random.choice("aeiouy")
        name += konsonant + vokal
    name += "gon von Ormbarst"
    return(name)

# zzz(von_ormbarst_namn(), 0.05)