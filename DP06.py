prijmeni = str(input("Zadej svoje příjmení a já ti řeknu kdo jsi:"))
def poznani_pohlavi (prijmeni):
    "Podle obsahu ová/ova na konci přijmení funkce pozná, že jde o ženu"
    if prijmeni.endswith("ová") or prijmeni.endswith ("ova"):
        print ("Jsi žena!")
    else:
        print ("Jsi muž!")
    return

poznani_pohlavi (prijmeni)
