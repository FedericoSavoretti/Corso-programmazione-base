#Chiedi un numero all'utente e somma i numeri da 1 fino al numero immesso.
i = 1
totale = 1
numero = int(input("Inserisci il numero: "))
while i <= numero:
    totale = totale + 1
    i = i + 1 
    print(totale)