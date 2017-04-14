from random import randrange

def hod_kostkou ():
    "Hazí kostkou náhodná čísla 1 až 6"
    cislo = randrange (1,7)
    print (cislo)
    return cislo

print ("Hraje první hráč")
a = hod_kostkou()

while True:
    if a !=6:
        hod_kostkou ()
    else:
        break
