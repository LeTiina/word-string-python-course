# tee ratkaisu tänne

def eka_sana(lause):
    sana = ""
    apuri = 0
    while True:
        if lause[apuri] == " ":
            break
        sana = sana + lause[apuri]
        apuri = apuri +1
    return sana

def toka_sana(lause):
    sana = ""
    sana2 = ""
    apuri = 0
    pituus = 1
    while True:
        if lause[apuri] == " ":
            while True:
                apuri = apuri +1
                if len(lause) == pituus:
                    return sana2
                if lause[apuri] == " ":
                    return sana2
                sana2 = sana2+lause[apuri]
                pituus = pituus +1
        sana = sana + lause[apuri]
        apuri = apuri +1
        pituus = pituus + 1

def vika_sana(lause):
    sana = ""
    apuri = -1

    while True:
        if lause[apuri] == " ":
            return sana
        sana = lause[apuri]+sana
        apuri = apuri -1

lause = "olipa kerran kauan sitten ohjelmoija"

print(eka_sana(lause)) # olipa
print(toka_sana(lause)) # kerran
print(vika_sana(lause)) # ohjelmoija
print(toka_sana("eka toka"))