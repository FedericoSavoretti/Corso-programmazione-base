#Ci sono 5 nomi: Alina, Bruno, Carlo, Dario, Emilio. 
#Chiedi una lettera all'utente. Stampa il nome corrispondente alla prima lettera. 
#Se non è nella lista stampa "you chose ... poorly".
lettera = input("Inserisci una lettera")
if(lettera == "A"):
    print("Alina")
else:
    if(lettera == "B"):
        print("Bruno")
    else:
        if(lettera == "C"):
            print("Carlo")
        else:
            if(lettera == "D"):
                print("Dario")
            else:
                    if(lettera == "E"):
                        print("Emilio")
                    else:
                        print("You choose poorly")    