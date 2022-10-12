n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))
if(n1 > 10):
    print("Fuori Scala")
if(n2 > 50):
    print("Troppo Grande")
else:
    if(n1 <= 10 and n2 <= 50):
        print("Tutto ok")