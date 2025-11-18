from random import randint
import time
import skatter
from skatter import k1, k2, k3, k4

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew']
enamn = ['den fördärvade', 'Bajs', 'McMillen', 'Döden', 'O´ Moriah', 'Kall']

class karaktar:
    def __init__(karaktar, namn, kp, sty, niva, inventarie):
        karaktar.namn = namn
        karaktar.kp = kp
        karaktar.sty = sty
        karaktar.niva = niva
        karaktar.inventarie = inventarie

tempkp = randint(1, 5)
tempsty = randint(5, 15)//tempkp
evigsakkvalitet = randint(1, 100)
if evigsakkvalitet >= 95:
    evigsakkvalitet = k4
elif evigsakkvalitet >= 80:
    evigsakkvalitet = k3
elif evigsakkvalitet > 60:
    evigsakkvalitet = k2
else:
    evigsakkvalitet = k1
sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]} {enamn[randint(0, len(enamn)-1)]}", tempkp, tempsty, 0, evigsakkvalitet[randint(0, len(evigsakkvalitet) - 1)])
print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)
print(f'Startföremål: {sp1.inventarie.namn} | Kvalitet: {sp1.inventarie.kvalitet}\n{sp1.inventarie.beskrivning}')

if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

while True:
    val = input('''Vad vill du göra?
                Kolla [R]yggsäcken
                Öppna en [D]örr
                Kolla [F]ärdigheter 
                -> ''')
    
