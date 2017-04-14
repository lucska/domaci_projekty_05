def vyhodnot (retezec_piskvorky):
    "Vyhodnocení piškvorek, funkce kouká, co obsahuje řetězec"
    if "xxx" in retezec_piskvorky:
        return "x"
    elif "ooo" in retezec_piskvorky:
        return "o"
    elif "-" not in retezec_piskvorky:
        return "!"
    else:
        return "-"

a = vyhodnot ("xoxoxoxox")
if a == "x":
    print ("Vyhrál hráč s křízky")
elif a == "o":
    print ("Vyhrál hráč s kolečky")
elif a == "!":
    print ("Remíza")
elif a == "-":
    print ("Hra pokračuje")
