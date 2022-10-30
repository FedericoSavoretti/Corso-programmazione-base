#Chiedi all'utente di indovinare un numero magico.
#Il numero magico è il numero 7.
#L'utente ha 10 tentativi.Se indovina stampa "Complimenti, hai indovinato!" Se non indovina stampa "Game over!" alla fine dei 10 tentativi
numeroinserito = 0
numeromagico = 7
tentativi = 0
while tentativi <11:
    tentativi = tentativi + 1
    numeroinserito = int(input("Inserisci il numero magico"))
    if (numeroinserito == numeromagico):
        print("Complimenti, hai indovinato!")
        tentativi <= 10
    else:
        if(tentativi > 10):
            print("Game over")