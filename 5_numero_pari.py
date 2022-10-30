#Chiedi all'utente un numero pari.
# Se il numero inserito è pari somma il numero inserito al numero 3 e restituisci il risultato.
# Se è dispari stampa la frase "hai inserito un numero dispari birbante!"
n = int(input("Inserisci un numero pari: "))
if (n%2 == 0):
    print(n+3)
else:
    print("Hai inserito un numero dispari birbante")