Ccount = 0
def CysCount(sequence):
    global Ccount
    text = sequence
    for i in range(len(text)):
        if text[i] == "C":
            Ccount+=1
    Ccount = Ccount/float(len(sequence))
    return Ccount
    Ccount = 0

print CysCount("ACCACAACTACAGCATCAHTCAHTC")
