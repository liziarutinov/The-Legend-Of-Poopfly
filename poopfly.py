from random import randint
import time
from skatter import skatt
from skatter import print_skatt
from skatter import k1, k2, k3, k4
from ormbarst_name_gen import von_ormbarst_namn

print('''
                                _____ _
                               |_   _| |__   ___
                                 | | | '_ \ / _ |
                                 | | | | | |  __/
                                 |_| |_| |_|\___|
             :::       :::::::::::::::::: ::::::::::::::    ::::::::::::
            :+:       :+:      :+:    :+::+:       :+:+:   :+::+:    :+:
           +:+       +:+      +:+       +:+       :+:+:+  +:++:+    +:+
          +#+       +#++:++# :#:       +#++:++#  +#+ +:+ +#++#+    +:+
         +#+       +#+      +#+   +#+#+#+       +#+  +#+#+#+#+    +#+
        #+#       #+#      #+#    #+##+#       #+#   #+#+##+#    #+#
       ############################ #############    #############
                                          __
                                    ___  / _|
                                   / _ \| |_
                                  | (_) |  _|
                                   \___/|_|
         :::::::::  ::::::::  :::::::: ::::::::: :::::::::::::    :::   :::
        :+:    :+::+:    :+::+:    :+::+:    :+::+:       :+:    :+:   :+:
       +:+    +:++:+    +:++:+    +:++:+    +:++:+       +:+     +:+ +:+
      +#++:++#+ +#+    +:++#+    +:++#++:++#+ :#::+::#  +#+      +#++:
     +#+       +#+    +#++#+    +#++#+       +#+       +#+       +#+
    #+#       #+#    #+##+#    #+##+#       #+#       #+#       #+#
   ###        ########  ######## ###       ###       #############
''')

input('Träd in i fängelshålan och ta med dig Poopfly:n på [RETUR] resan')

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew', 'gon', 'Filip', 'Holger'] 
enamn = [', den fördärvade', ' Bajs', ' McMillen', ' Döden', 'Nilsson', 'Rosencrantz', ' O´ Moriah', ' Kall', ' Von Ormbarst', ', den trosfanatiska', ', den skurna', ', den oförfärad', ', den oupplysta', ', den enigmatiska', ', den godtyckliga']

class karaktar: #Strukturen för spelarkaraktären
    bas_kp = randint(5, 10) #Basvärde för karaktärens KP
    bas_sty = randint(25, 50)//bas_kp #Basvärde för karaktärens STY, delat på bas_kp för att balansera
    bas_niva = 0
    kpmod = 0
    stymod = 0
    nivamod = 0
    skada = 0
    inventarie = []
    def __init__(self, namn, kp, sty, niva):
        self.namn = namn
        self.kp = kp
        self.sty = sty
        self.niva = niva

    def ge_stats(self):
        self.kpmod = 0
        self.stymod = 0
        self.nivamod = 0
        stymult = 1
        kpmult = 1
        for i in range(len(self.inventarie)): #applicerar föremålens modifikationer på karaktären, förändringarna kommer från filen skatter.py
            if self.inventarie[i - 1].mod_ar_mult == True:
                stymult += self.inventarie[i - 1].kpmod
                kpmult += self.inventarie[i - 1].stymod
            else:
                self.kpmod += self.inventarie[i - 1].kpmod
                self.stymod += self.inventarie[i -1].stymod
                self.nivamod += self.inventarie[i - 1].nivamod
        
        self.niva = self.bas_niva + self.nivamod #spelarens totala nivå
        if self.bas_kp + self.kpmod * kpmult < 1:
                self.kp = 1
        else:
            self.kp = self.bas_kp + self.kpmod * kpmult + (self.niva * 2)
        self.sty = self.bas_sty + self.stymod * stymult + (self.niva * 2)
        if self.niva >= 10: #En check som kollar om spelaren vunnit eller förlorat varje gång det är möjligt.
            if self.kp -self.skada < 1:
                quit('Du vann och dog samtidigt... galet...')
            quit('Du vann spelet!!!!!!!!')
        elif self.kp - self.skada < 1:
            quit('Förlust: Du har tagit mer träffar än du har KP!')
        synergi_array = [] #Används för att kolla synergieffekter mellan föremål i inventarien
        for i in range(len(self.inventarie)): #SYNERGIER FUNKAR INTE ÄNNU
            if self.inventarie[i].synergi_id != 0:
                synergi_array.append(self.inventarie[i].synergi_id)
        synergi_array.sort()
        print(synergi_array)
        for i in range(1, len(synergi_array) - 1):
            if synergi_array[i] == synergi_array[i - 1]:
                if synergi_array[i] == 1:
                    self.inventarie.remove(skatt('Tändare', 0, 1, 0, '"Hmmm. Jag undrar om dem kan brinna..."', 1))
                    self.inventarie.remove(skatt('Spraydeoderant', 1, 0, 0, '"Teknikelevernas mardröm"', 1))
                    self.inventarie.append(skatt('improviserad ELDKASTARE', -2, 5, 0, '"BOCKEN BRINNER!!!"', 0)) 



def avskaffa_skatt(self): #Funktion för att ta bort/byta ut ett föremål i spelarens inventarie
    output = ''
    for i in range(0, len(self.inventarie)):
        output += f'{i + 1}. {print_skatt(self.inventarie[i])}\n\n'
    print(output)
    while True:
        val = input(f'Vilken skatt i din ryggsäck vill du byta ut??->')
        if int(val) in range(1, len(self.inventarie) + 1):
            if input(f'Är du säker på att du vill byta ut {self.inventarie[int(val) - 1].namn}? J/N ->').upper() == 'J':
                self.inventarie.pop(int(val) - 1)
                return()
            else:
                print('Skriv siffran som representerar föremålet du vill byta ut (1, 2, 3, 4, 5, 6)')

def tilvinna_skatt(self, skatt): #Funktion för att lägga till ett föremål i spelarens inventarie
    self.inventarie.append(skatt)
    if len(self.inventarie) > 5:
        avskaffa_skatt(self)




sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]}{enamn[randint(0, len(enamn)-1)]}", karaktar.bas_kp, karaktar.bas_sty, karaktar.bas_niva)#Skapar rollpersonen utifrån klassen karaktar. Skapar namn från listorna fnamn och enamn.
if sp1.namn[0] == 'g':
    sp1.namn = von_ormbarst_namn() #Speciell namn-generator för namn som börjar med g, för att få mer passande namn för Von Ormbarst

sp1.inventarie += [skatt('Spray Deoderant', 1, 0, 0, '"Teknikelevernas mardröm"', 1), skatt('Tändare', 0, 1, 0, '"Hmmm. Jag undrar om dem kan brinna..."', 1)]
foremal_kvalitet = randint(1, 100) #Bestämmer föremåls kvalitet för evighetsföremålet
if foremal_kvalitet >= 96:
    foremal_kvalitet = k4
elif foremal_kvalitet >= 81:
    foremal_kvalitet = k3
elif foremal_kvalitet > 61:
    foremal_kvalitet = k2
else:
    foremal_kvalitet = k1

sp1.inventarie.append(foremal_kvalitet[randint(0, len(foremal_kvalitet)-1)]) #Föremålet läggs till i spelare 1s inventraie
print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)
print(f'Startföremål: {sp1.inventarie[0].namn} | Kvalitet: {sp1.inventarie[0].kvalitet}\n{sp1.inventarie[0].beskrivning}')

if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

#RESTEN AV INTROT

#Alla våra monster:

class monster: #strukturen alla monster följer
    def __init__(monster, genus, monstertyp, sty, kp):
        monster.genus = genus
        monster.monstertyp = monstertyp
        monster.sty = sty
        monster.kp = kp

monsteralternativ = [ #möjliga fiender
    monster('En vild', 'Guldfisk', 2, 1),
    monster('En vild', 'Goblin', 4, 1),
    monster('En vild', 'Häxa', 6, 1),
    monster('Ett vilt', 'Troll', 8, 1),
    monster('En vild', 'Rikard', 10, 1),
    monster('En galen', 'Blottare', 6, 1),
    monster('En kittel', 'fladdermöss', 4, 1)
]

bossmonsteralternativ = [ # möjliga bossar
    monster('Den store och mäktiga fritidsledaren: ', 'Mojje', 100, 100),
    monster('Den fruktansvärt (gulliga): ', 'Bleh', 77, 77),
    monster('"Jag skulle behöva en önskan just nu..."', 'Mortecai', 89, 50),
    monster('Den', 'den', 1, 1)
]

attackbeskrivning = [f'slår {sp1.namn}', f'sparkar {sp1.namn}', f'klöser {sp1.namn} med tånaglarna', f'biter {sp1.namn}', f'slickar {sp1.namn}', 'sticker {sp1.namn}', 'krossar {sp1.namn}',] #kul beskrivning för hur spelaren attackeras.

while True: #Hela spelloopen
    sp1.ge_stats()
    rumstyp = ['monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'skattkammare', 'skatterum', 'bossrum', 'bossrum', 'läkerum'] #lista med möjliga rumstyper. rumsantalen öker/sänker oddsen att stöta på vissa rum
    while len(rumstyp) > 3: #tar bort rum tills det bara är tre kvar
        rumstyp.pop(randint(0, len(rumstyp)-1)) 
    dorrbeskrivningar = [] #tom lista för att lagra dörrbeskrivningar, gör spelet svårare då det inte är uppenbart vilket rum som dyker upp.
    for i in rumstyp:
        if i == 'monsterrum':
            dorrbeskrivningar.append('mörk dörr med blodfläckar...')
        elif i == 'skattkammare':
            dorrbeskrivningar.append('trädörr med en gyllene ram...')
        elif i == 'skatterum':
            dorrbeskrivningar.append('gyllene dörr med en träram...')
        elif i == 'bossrum':
            dorrbeskrivningar.append('asstor port med en dödskalle på...')
        elif i == 'läkerum':
            dorrbeskrivningar.append('dörr med ett välkomnande ljus bakom...')
        else:
            print('något har gått riktigt fel här... slut på det roliga :/') #errormeddelande som inte bör dyka upp.
    print(f"du ser tre dörrar: \n en {dorrbeskrivningar[0]} \n en {dorrbeskrivningar[1]} \n och en {dorrbeskrivningar[2]}")

    while True: #meny innan strid
        val = input('''Vad vill du göra?
                    Kolla [R]yggsäcken
                    Öppna en [D]örr
                    Kolla [F]ärdigheter 
                    -> ''').upper()
        
        if val == 'R':
            for i in range(len(sp1.inventarie)):
                print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')
        elif val == 'D':
            while True:
                val = input(f'Vilken dörr vill du öppna? \n [1] {dorrbeskrivningar[0]} \n [2] {dorrbeskrivningar[1]} \n [3] {dorrbeskrivningar[2]} \n [4] Avbryt \n ->')
                if val in ['1', '2', '3', '4']:
                    break
                else:
                    print('Ogiltigt val: välj igen') #om spelaren inte väljer ett giltigt val.
                    continue
            if val in ['1', '2', '3']: #om spelaren väljer att öppna en dörr
                print(f'{sp1.namn} kliver in i ett {rumstyp[int(val)-1]}') #rumstypen avsjöjas för spelaren
                time.sleep(1)
                break

        elif val == 'F': #printar spelarens färdigheter
            print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}')

        else:
            continue
        
# RUMSTYPER OCH HÄNDELSER

    # MONSTERRUM

    if rumstyp[int(val)-1] == 'monsterrum':
        sp1.ge_stats() #uppdaterar spelarens stats en funktion
        fiende = monsteralternativ[randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum
        print(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        print(f"Den har styrkan {fiende.sty}")
        print(f"{sp1.namn}{plural} styrka är {sp1.sty}")

        time.sleep(0.5)

        while True: #stridssekvensen
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [M]onstret {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')
                elif val == 'M':
                    break
                elif val == 'F':
                    print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}')
                else:
                    continue

        if sp1.sty > fiende.sty: #kollar om spelaren vinner
            print(f"{sp1.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n\n")
            sp1.bas_niva += 1 #sp1 går upp en nivå
        elif sp1.sty == fiende.sty: 
            print(f"Det var en svår strid, utan segrare. Du tar ingen skada men går inte upp en nivå. \n\n")
        else: #om selaren varken vinner 
            print(f"{sp1.namn} blev besegrad av {fiende.monstertyp} och förlorade 1 kp. \n\n")
            sp1.skada += 1

        time.sleep(0.5)

        print(f"{sp1.namn} har {sp1.kp - sp1.skada} kp kvar.")
        print(f"{sp1.namn} är nivå {sp1.niva}.")
    
    #SKATTKAMMARE, rum att få skatter i

    elif rumstyp[int(val)-1] == 'skattkammare': 
        foremal_kvalitet = randint(1, 100)
        while True:
            if foremal_kvalitet >= 96:
                if len(k4) > 0:
                    tillvunnet_foremal = k4[randint(0, len(k4) - 1)]
                    k4.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 81
                    continue
            elif foremal_kvalitet >= 81:
                if len(k3) > 0:
                    tillvunnet_foremal = k3[randint(0, len(k3) - 1)]
                    k3.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 61
                    continue
            elif foremal_kvalitet > 61:
                if len(k2) > 0:
                    tillvunnet_foremal = k2[randint(0, len(k2) - 1)]
                    k2.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 1
                    continue
            elif len(k1) > 0:
                tillvunnet_foremal = k1[randint(0, len(k1) - 1)]
                k1.remove(tillvunnet_foremal)
            else:
                tillvunnet_foremal = skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."')
            break
        mod = 'mod'
        if skatt.mod_ar_mult == True:
            mod = 'mult'
        print('I skattkammaren finns det:\n')
        time.sleep(1)
        print(f'  {print_skatt(tillvunnet_foremal)}')
        while True:
            val = input('\nVill du plocka upp den? J/N ->').upper()
            if val == 'J':
                tilvinna_skatt(sp1, tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                print('Skriv in [J]a eller [N]ej')

    # SKATTERUM, rum att betala skatt i

    elif rumstyp[int(val)-1] == 'skatterum':
        print(f'{sp1.namn} kliver in i en mörk skattkammare')
        time.sleep(0.5)
        print(f'{sp1.namn} ser en dvärg i andra änden av rummet')
        print('"gadd eller kladd"')
        while True:
            val = input('Vad vill du betala i skatt? 1 [S]katt eller 2 [K]P -> ').upper()
            if val == 'S' or val == 'K':
                break
            else:
                print('Du måste skriva S eller K')
                continue 
        if val == 'K':
            sp1.skada += 2
        elif val == 'S':
            avskaffa_skatt(sp1)

    #EN BOSS

    elif rumstyp[int(val)-1] == 'bossrum':
        sp1.ge_stats()
        fiende = bossmonsteralternativ[randint(0, len(bossmonsteralternativ)-1)]
        print(f'I ett bossrum kommer turer att utkämpas tills spelaren eller bossen är döda, eller spelaren lyckas fly. Spelaren kommer bli slagen upp till bossens sty och spelaren slår upp till sin sty, mellan varje tur kan föremål användas.')
        print(f'Plötsligt dyker {fiende.genus} {fiende.monstertyp} upp och ger dig en fördärvande blick!')
        
        while fiende.kp > 0:
            print(f'{fiende.monstertyp} gör upp till {fiende.sty} skada!!!')
            print(f'{fiende.monstertyp} har {fiende.kp} kp')

            while True:
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [B]ossen {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')
                elif val == 'B':
                    break
                elif val == 'F':
                    print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}')
                else:
                    continue


            slag = randint(1, fiende.sty)
            print(f'{fiende.monstertyp} {attackbeskrivning[randint(0, len(attackbeskrivning)-1)]} och gör {slag} skada!')
            sp1.skada += slag

            slag = randint(1, sp1.sty)
            print(f'{sp1.namn} slår {fiende.monstertyp} och gör {slag} skada')
            fiende.kp -= slag
            sp1.ge_stats()

        print(f'{sp1.namn} besegrade {fiende.monstertyp}!')
        foremal_kvalitet = randint(1,100)
        while True:
            if foremal_kvalitet >= 51:
                if len(k4) > 0:
                    tillvunnet_foremal = k4[randint(0, len(k4) - 1)]
                    k4.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 1
                    continue
            elif foremal_kvalitet >= 1:
                if len(k3) > 0:
                    tillvunnet_foremal = k3[randint(0, len(k3) - 1)]
                    k3.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 0
                    continue
            elif foremal_kvalitet > 0:
                if len(k2) > 0:
                    tillvunnet_foremal = k2[randint(0, len(k2) - 1)]
                    k2.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 0
                    continue
            elif len(k1) > 0:
                tillvunnet_foremal = k1[randint(0, len(k1) - 1)]
                k1.remove(tillvunnet_foremal)
            else:
                tillvunnet_foremal = skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."')
            break
        mod = 'mod'
        if skatt.mod_ar_mult == True:
            mod = 'mult'
        print('I skattkammaren finns det:\n')
        time.sleep(1)
        print(f'  {print_skatt(tillvunnet_foremal)}')
        while True:
            val = input('\nVill du plocka upp den? J/N ->').upper()
            if val == 'J':
                tilvinna_skatt(sp1, tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                print('Skriv in [J]a eller [N]ej')

    
    # LÄKERUM, spelaren helas

    elif rumstyp[int(val)-1] == 'läkerum': 
        sp1.skada = sp1.skada - randint(1,3)
        if sp1.skada <= 0:
            sp1.skada = 0
        print('Du är nu hel!')