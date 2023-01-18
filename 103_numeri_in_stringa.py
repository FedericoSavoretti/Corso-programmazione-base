i = 0
c = 0
somma = 0
stringa = str(input("Inserisci una stringa di numeri: "))
n = len(stringa)
while i < n:
    c = stringa[i]
    if(int(c)):
        i = i + 1
    else:
        print("Hai inserito una lettera")
        break
i = 0
while i < n:
    c = stringa[i]
    somma = somma + int(c)
    i = i + 1
print(somma)