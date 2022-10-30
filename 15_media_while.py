#Calcola la media di tutti i numeri che l'utente ha inserito fino a quel momento.
#Quando l'utente inserisce il numero 0 allora stampa il risultato.
i = 0
numero = 0
media = 0
while True:
    numero = int(input("Inserisci un numero: "))
    media = media + numero
    if(numero == 0):
        break
    i = i + 1 
media = media/i
print(media) 