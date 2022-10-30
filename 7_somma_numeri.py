#Chiedi all'utente di inserire 3 numeri.
#Se la somma è maggiore di 10 allora restituisci il numero più grande. 
#Se invece non è maggiore di 10 restituisci la somma dei 3 numeri.
n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))
n3 = int(input("Inserisci il terzo numero"))
somma = (n1 + n2 + n3)
if(somma > 10):
    if(n1 > n2):
        if(n1 > n3):
            print("Il numero più grande è " , n1)
    if(n2 > n1):
        if(n2 > n3):
            print("Il numero più grande è " , n2)
    if(n3 > n2):
        if(n3 > n1):
            print("Il numero più grande è " , n3)
else:
    print("La somma è " , somma)