import random
from random import randint

def von_ormbarst_namn():
    stavelser = randint(1, 2) #längd på namnet
    name = ""
    for i in range(stavelser):
        if i == 0:
            konsonant = random.choice("bcdfghjklmnpqrstvwxz").upper() #lista med konsonanter, stor första bokstav
        else:
            konsonant = random.choice("bcdfghjklmnpqrstvwxz") 
        vokal = random.choice("aeiouy")
        name += konsonant + vokal #sätter ihop ett slumpnamn
    name += "gon von Ormbarst"
    return(name) #returnerar det slumpade namnet