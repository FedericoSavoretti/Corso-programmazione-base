stringa = str(input("inserisci una frase: "))
n = len(stringa)
c= ''
i = 0
vocale = 0
while i < n:
    c = stringa[i]
    if((c == "a") or (c == "A")):
        vocale = vocale + 1
    if((c == "e") or (c == "E")):
        vocale = vocale + 1
    if((c == "i") or (c == "I")):
        vocale = vocale + 1
    if((c == "o") or (c == "O")):
        vocale = vocale + 1
    if((c == "u") or (c == "U")):
        vocale = vocale + 1
    i = i + 1
print(vocale)