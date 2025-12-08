from random import randint
class skatt:
    kvalitet = 1
    mod_ar_mult = False
    def __init__(skatt, namn, kpmod, stymod, nivamod, beskrivning):
        skatt.namn = namn
        skatt.kpmod = kpmod
        skatt.stymod = stymod
        skatt.nivamod = nivamod
        skatt.beskrivning = beskrivning

def print_skatt(sak):
    mod = 'mod'
    if sak.mod_ar_mult == True:
        mod = 'mult'
    output = f' {sak.namn} | Kvalitet: {sak.kvalitet}\n  {sak.beskrivning}\n   KP {mod}: {sak.kpmod} | STY {mod}: {sak.stymod} | Nivå mod {sak.nivamod}'
    return(output)

# skatt('NAMN', kp modifier, sty modifier, niva modifier, '"Beskrivning"')
#Kvalitet 1 föremål
k1 = [
skatt('Teleskop', 0, 0, 0, '"Ökad sikt"'),
skatt('Spade', 0, 1, 0, '"Gräva gräva hål!"'),
skatt('Nagelfil', 0, 2, 0, '"Skönhet dödar!"'),
skatt('Tändare', 0, 1, 0, '"Hmmm. Jag undrar om dem kan brinna..."'),
skatt('Spray Deoderant', 1, 0, 0, '"Teknikelevernas mardröm"'),
skatt('Gambeson', 2, 0, 0, '"En fint kviltad linrustning"')
]

#Kvalitet 2 föremål
k2 = [
skatt('Raket i en burk', -1, 2, 0, '"Jag förstår inte riktigt hur man fick in den..."'),
skatt('Pandoras ask', randint(-2, 4), randint(-5, 5), randint(0, 1), '"Slumpmässig egenskapsförändring"'),
skatt('Ringbrynja', 3, 0, 0, '"En nitad ringbrynja"'),
skatt('Sabel', 0, 3, 0, '"Läderlindat handtag och ett skarpt blad"'),
skatt('Kofot', 0, 3, 0, '"Muuuuuu..."')
]
for i in k2: 
    i.kvalitet = 2 #Ger alla items i listan k2 kvalitetvärde 2

#Kvalitet 3 föremål
k3 = [
skatt('Sten', -1, 5, 0, '"Hur kan en sten gråta?!"'),
skatt('Swiss army knife', 0, 6, 0, "Undrar varför pappor älskar såna.."),
skatt('Ring', 2, 2, 2, '"Det är ju jag!" - Alwin Ring \n "En skapades för att styra alla"'),
skatt('Liten Anton', 1, 5, 2, '"Bassisten i Ormbarst fast mini version"'),
skatt('Minikit', 0, 4, 2, '"Kai"')
]
for i in k3:
    i.kvalitet = 3 #Ger alla items i listan k3 kvalitetvärde 3

#Kvalitet 4 föremål
k4 = [
skatt('Helig utplånare', 0, 2, 1, '"Hellre detta än Universumsförstörare"'),
skatt('Universumförstare', 2, 0, 1, '"Hellre detta än Helig utplånare"'),
skatt('Glasögon', 1.4, 1.4, -1, '"20/20 syn... minus erfarenhet"'),
skatt('Lillens spratt', 1.1, 1.2, 0, '"Bam bam!"'),

]
for i in k4:
    i.kvalitet = 4 #Ger alla items i listan k4 kvalitetvärde 4
    i.mod_ar_mult = True
