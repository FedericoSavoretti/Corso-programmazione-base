n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))
n3 = int(input("Inserisci il terzo numero"))
somma = (n1 + n2 + n3)
if(somma > 10):
    if(n1 > n2 and n3):
        print(n1)
    if(n2 > n1 and n3):
        print(n2)
    if(n3 > n2 and n1):
        print(n3)
else:
    print(somma)