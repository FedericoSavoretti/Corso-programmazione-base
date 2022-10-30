#Chiedi all'utente quante operazioni vuole fare con la calcolatrice. 
#Successivamente chiederi 2 numeri e l'operazione da effettuare. 
#l'operazione da effettuare è tra somma (1), sottrazione (2), divisione (3), moltiplicazione (4). 
#Se l'utente vuole effettuare più di una operazione allora al risulto ottenuto applica l'operazione scelta di volta in volta immessa dall'utente. 
#Alla fine delle operazioni stampa il risultato.
#Presta attenzione per la divisione per zero e stampa il messaggio di errore "Non puoi dividere per zero!" ed esci dal programma nel caso.
#Se l'utente sceglie un operazione non contemplata effettua la somma.
operazione = 0
numero1= 0
numero2= 0
risultato= 0
numero1 = int(input("Inserisci il primo numero"))
numero2 = int(input("Inserisci il secondo numero"))
print("1 = somma")
print("2 = sottrazione")
print("3 = divisione")
print("4 = moltiplicazione")
operazione = int(input("Ora scegli l'operazione da fare"))
while True:
    if operazione == 1:
        risultato = numero1 + numero2
        break
    if operazione == 2:
        risultato = numero1 - numero2
        break
    if operazione == 3:
        risultato == numero1 / numero2
        break
    if operazione == 4:
        risultato = numero1 * numero2
        break
    if operazione > 4:
        risultato = numero1 + numero2
        break
if numero1 == 0:
    print("Non puoi dividere per zero!")
if numero2 == 0:
    print("Non puoi dividere per zero!")
else:
    print("Il risultato è " , risultato)