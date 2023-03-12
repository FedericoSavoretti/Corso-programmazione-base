import random


#introduzione
while True:
    risposta_iniziale = input('Paolo Bonolis:"Benvenuto, desideri giocare ad avanti un altro?" (digitare si se si vuole procedere) ')
    if(risposta_iniziale == "si" or risposta_iniziale == "Si"):
        break
    else:
        print("ERROR 404")
        continue


#inizializzo le variabili per il primo livello
montepremi_vinto : int = 0
tema_giocati : int = 0
tema_1 : int = 0
tema_2 : int = 0


#primo livello
print('Paolo Bonolis:"Benvenuto al primo livello..."')
while True:


    #Il pc sceglia il tema del gioco
    tema = random.randrange(0,2)


    #inizializzo le variabili del primo livello
    minigioco : int = 0
    domanda_minigioco : int = 0
    risposta = ''
    pidigozzo_Random : int = 0
    pidigozzo_scelto : int = 0
    risposta_minigioco : int = 0
    ripetizione_domanda_0 : int = 0
    ripetizione_domanda_1 : int = 0
    ripetizione_domanda_2 : int = 0
    ripetizione_domanda_3 : int = 0
    ripetizione_domanda_4 : int = 0
    i : int = 0
    risposte_sbagliate : int = 0
    risposte_giuste : int= 0
    ciclo_finale : int = 0
    risposte_sbagliate_finale : int= 8

    #minigiochi
    while tema_giocati == 1:
        minigioco = random.randrange(0,4)
        domanda_minigioco = random.randrange(0,2)
        if(minigioco == 0):
            print("!!!MINI GIOCO!!!")
            print('Paolo Bonolis:" Il personaggio che è appena entrato è... lo iettatore "')
            print('Paolo Bonolis:" Le regole sono semplici: se rispondi in modo corretto continui a giocare, se rispondi in modo errato, hai perso "')
            if(domanda_minigioco == 0):
                print('''Lo iettatore:"La domanda è "Qual era il nome della ragazzina posseduta dal demonio ne L’esorcista?"''')
                print('Lo iettatore:"La risposta a è "Regan MacNeil"')
                print('Lo iettatore:"La risposta b è "Regan Mcneal"')
                risposta = input('Paolo Bonolis:"Cosa scegli?: "')
                if(risposta == "a" or risposta == "A"):                        
                    print('Lo iettatore:"Il minigioco è finito... hai vinto!"')
                    break
                if(risposta == "b" or risposta == "B"):
                    print('Lo iettatore:"Il minigioco è finito... hai perso!"')
                    risposte_sbagliate_finale = 0
            if(domanda_minigioco == 1):
                print('Lo iettatore:"La domanda è "Quale capitolo della saga di venerdì 13 Jason inizia a usare la maschera da hockey?"')
                print('Lo iettatore:"La risposta a è "Venerdì 13 parte II- L’assassino ti siede accanto"')
                print('Lo iettatore:"La risposta b è "Venerdì 13 – Capitolo finale"')
                risposta = input('Lo iettatore:"Cosa scegli?: "')
                if(risposta == "b" or risposta == "B"):
                    print('Lo iettatore:"Il minigioco è finito... hai vinto!"')
                    break
                if(risposta == "a" or risposta == "A"):
                    print('Lo iettatore:""Il minigioco è finito... hai perso!"')
                    risposte_sbagliate_finale = 0
            tema_giocati = tema_giocati + 1  
        if(minigioco == 1):
            print("!!!MINI GIOCO!!!")
            print('Paolo Bonolis:"Il personaggio che è appena entrato è La Regina del Web"')
            print('La Regina del Web:"Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso"')
            if(domanda_minigioco == 0):
                print('La Regina del Web:"La domanda è "per cosa sta https?"')
                print('La Regina del Web:"La risposta a è "Hyper Text Transfer Protocol Secure"')
                print('La Regina del Web:"La risposta b è "HyperText Transfer Protocol"')
                risposta = input('La Regina del Web:"Cosa scegli?: "')
                if(risposta == "a" or risposta == "A"):
                    print('La Regina del Web:""Il minigioco è finito... hai vinto!"')
                    risposta_minigioco = risposta_minigioco + 1
                if(risposta == "b" or risposta == "B"):
                    print('La Regina del Web:"Il minigioco è finito... hai perso!"')
                    risposte_sbagliate_finale = 0
            if(domanda_minigioco == 1):
                print('La Regina del Web:"La domanda è "in che anno è stato creato whatsapp"')
                print('La Regina del Web:"La risposta a è "2008"')
                print('La Regina del Web:"La risposta b è "2009"')
                risposta = input('La Regina del Web:""Cosa scegli?: "')
                if(risposta == "a" or risposta == "A"):
                    print('La Regina del Web:""Il minigioco è finito... hai perso!"')
                    risposte_sbagliate_finale = 0
                if(risposta == "b" or risposta == "B"):
                    print('La Regina del Web:"Il minigioco è finito... hai vinto!"')
                    risposta_minigioco = risposta_minigioco + 1
            while risposta_minigioco == 1:
                print('Paolo Bonolis:" Complimenti ha superato il minigioco, ora scelga un pidigozzo"')
                print('Paolo Bonolis:" Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9"')
                pidigozzo_scelto = int(input('Paolo Bonolis:"Quale scegli?: "'))
                if(pidigozzo_scelto > 9):
                    continue
                else:
                    pidigozzo_Random = random.randrange(1,10)
                    if(pidigozzo_Random == 1):
                        montepremi_vinto = montepremi_vinto + 10000
                        print("Hai vinto: 10000 €")
                    if(pidigozzo_Random == 2):
                        montepremi_vinto = montepremi_vinto + 15000
                        print("Hai vinto: 15000 €")
                    if(pidigozzo_Random == 3):
                        montepremi_vinto = montepremi_vinto + 20000
                        print("Hai vinto: 20000 €")
                    if(pidigozzo_Random == 4):
                        montepremi_vinto = montepremi_vinto + 25000 
                        print("Hai vinto: 25000 €")
                    if(pidigozzo_Random == 5):
                        montepremi_vinto = montepremi_vinto + 30000 
                        print("Hai vinto: 30000 €")
                    if(pidigozzo_Random == 6):
                        montepremi_vinto = montepremi_vinto + 40000 
                        print("Hai vinto: 40000 €")
                    if(pidigozzo_Random == 7):
                        montepremi_vinto = montepremi_vinto + 50000 
                        print("Hai vinto: 50000 €")
                    if(pidigozzo_Random == 8):
                        montepremi_vinto = montepremi_vinto + 75000
                        print("Hai vinto: 75000 €")
                    if(pidigozzo_Random == 9):
                        montepremi_vinto = montepremi_vinto + 150000 
                        print("Hai vinto: 150000 €")
                    print('Paolo Bonolis:"Il tuo montepremi attuale ammonta a" ' , montepremi_vinto , "€")
                    tema_giocati = tema_giocati + 1
                    break
            if(risposta_minigioco == 1):
                break
        if(minigioco == 2):
            print("!!!MINI GIOCO!!!")
            if(domanda_minigioco == 0):
                print('''Paolo Bonolis:"Il personaggio che è appena entrato è L'Atleta totale italiano"''')
                print('''L'Atleta totale italiano:"Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso"''')
                print('''L'Atleta totale italiano:"la domanda è: "Quale numero di maglia indossava Lionel Messi al suo esordio con il Barca nel 2004?"''')
                print('''L'Atleta totale italiano:"La risposta a è "10"''')
                print('''L'Atleta totale italiano:"La risposta b è "7"''')
                print('''L'Atleta totale italiano:"La risposta c è "30"''')
                print('''L'Atleta totale italiano:"La risposta d è "5"''')
                risposta = input('''L'Atleta totale italiano:"Cosa scegli?: "''')  
                if(risposta == "a" or risposta == "A"):
                    print('''L'Atleta totale italiano:"Il minigioco è finito... hai perso!"''')
                    risposte_sbagliate_finale = 0
                if(risposta == "b" or risposta == "B"):
                    print('''L'Atleta totale italiano:"Il minigioco è finito... hai perso!"''')
                    risposte_sbagliate_finale = 0
                if(risposta == "c" or risposta == "C"):
                    print('''L'Atleta totale italiano:"Il minigioco è finito... hai vinto!"''')
                    risposta_minigioco = risposta_minigioco + 1
                if(risposta == "d" or risposta == "D"):
                    print('''L'Atleta totale italiano:"Il minigioco è finito... hai perso!"''')
                    risposte_sbagliate_finale = 0
                if(domanda_minigioco == 1):
                    print("Il personaggio che è appena entrato è L'Atleta totale italiano")
                    print('''L'Atleta totale italiano:"Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso"''')
                    print('''L'Atleta totale italiano:'la domanda è: "Quale numero di maglia indossava Cristiano Ronaldo allo Sporting Lisbona?"''')
                    print('''L'Atleta totale italiano:"La risposta a è "7"''')
                    print('''L'Atleta totale italiano:"La risposta a è "11"''')
                    print('''L'Atleta totale italiano:"La risposta a è "13"''')
                    print('''L'Atleta totale italiano: "La risposta a è "28"''')
                    risposta = input('''L'Atleta totale italiano:"Cosa scegli?: "''')  
                    if(risposta == "a" or risposta == "A"):
                        print('''L'Atleta totale italiano:"Il minigioco è finito... hai perso!"''')
                        risposte_sbagliate_finale = 0
                    if(risposta == "b" or risposta == "B"):
                        print('''L'Atleta totale italiano:"Il minigioco è finito... hai perso!"''')
                        risposte_sbagliate_finale = 0
                    if(risposta == "c" or risposta == "C"):
                        print('''L'Atleta totale italiano:"Il minigioco è finito... hai perso!"''')
                        risposte_sbagliate_finale = 0
                    if(risposta == "d" or risposta == "D"):
                        print('''L'Atleta totale italiano:"Il minigioco è finito... hai vinto!"''')
                        risposta_minigioco = risposta_minigioco + 1
            while risposta_minigioco == 1:
                print('Paolo Bonolis: "Complimenti ha superato il minigioco, ora scelga un pidigozzo" ')
                print('Paolo Bonolis:"Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9"')
                pidigozzo_scelto = int(input('Paolo Bonolis:"Quale scegli?: "'))
                if(pidigozzo_scelto > 9):
                    continue
                else:
                    pidigozzo_Random = random.randrange(1,10)
                    if(pidigozzo_Random == 1):
                        montepremi_vinto = montepremi_vinto + 10000
                        print("Hai vinto: 10000 €")
                    if(pidigozzo_Random == 2):
                        montepremi_vinto = montepremi_vinto + 15000
                        print("Hai vinto: 15000 €")
                    if(pidigozzo_Random == 3):
                        montepremi_vinto = montepremi_vinto + 20000
                        print("Hai vinto: 20000 €")
                    if(pidigozzo_Random == 4):
                        montepremi_vinto = montepremi_vinto + 25000 
                        print("Hai vinto: 25000 €")
                    if(pidigozzo_Random == 5):
                        montepremi_vinto = montepremi_vinto + 30000 
                        print("Hai vinto: 30000 €")
                    if(pidigozzo_Random == 6):
                        montepremi_vinto = montepremi_vinto + 40000 
                        print("Hai vinto: 40000 €")
                    if(pidigozzo_Random == 7):
                        montepremi_vinto = montepremi_vinto + 50000 
                        print("Hai vinto: 50000 €")
                    if(pidigozzo_Random == 8):
                        montepremi_vinto = montepremi_vinto + 75000
                        print("Hai vinto: 75000 €")
                    if(pidigozzo_Random == 9):
                        montepremi_vinto = montepremi_vinto + 150000 
                        print("Hai vinto: 150000 €")
                    print("Il tuo montepremi attuale ammonta a" , montepremi_vinto , "€")
                    tema_giocati = tema_giocati + 1 
                    break
            if(risposta_minigioco == 1):
                break
        if(minigioco == 3):
            print("!!!MINI GIOCO!!!")
            print('Paolo Bonolis:"Il personaggio che è appena entrato è Lo Scienziato Pazzo"')
            print('Lo Scienziato Pazzo"Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso"')
            if(domanda_minigioco == 0):
                print('Lo Scienziato Pazzo:"La domanda è "in base a cosa sono ordinati gli elementi chimici della tavola periodica sono ordinati?"')
                print('Lo Scienziato Pazzo:"La risposta a è "secondo il valore crescente del numero atomico"')
                print('Lo Scienziato Pazzo:"La risposta b è "secondo il valore crescente della massa atomica"')
                risposta = input('Lo Scienziato Pazzo"Cosa scegli?: "')
                if(risposta == "a" or risposta == "A"):
                    print('Lo Scienziato Pazzo"Il minigioco è finito... hai vinto!"')
                    risposta_minigioco = risposta_minigioco + 1
                if(risposta == "b" or risposta == "B"):
                    print('Lo Scienziato Pazzo:"Il minigioco è finito... hai perso!"')
                    risposte_sbagliate_finale = 0
            if(domanda_minigioco == 1):
                print('Lo Scienziato Pazzo:"La domanda è "il fosforo nella tavola periodica è rappresentato da"')
                print('Lo Scienziato Pazzo:"La risposta a è "Fs"')
                print('Lo Scienziato Pazzo:"La risposta b è "P"')
                risposta = input('Lo Scienziato Pazzo:"Cosa scegli?: "')
                if(risposta == "b" or risposta == "B"):
                    print('Lo Scienziato Pazzo:"Il minigioco è finito... hai vinto!"')
                    risposta_minigioco = risposta_minigioco + 1
                if(risposta == "a" or risposta == "A"):
                    print('Lo Scienziato Pazzo:"Il minigioco è finito... hai perso!"')
                    risposte_sbagliate_finale = 0
            if(risposte_sbagliate_finale == 0):
                break
            while risposta_minigioco == 1:
                print('Paolo Bonolis: "Complimenti ha superato il minigioco, ora scelga un pidigozzo" ')
                print('Paolo Bonolis:"Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9"')
                pidigozzo_scelto = int(input('Paolo Bonolis:"Quale scegli?: "'))
                if(pidigozzo_scelto > 9):
                    continue
                else:
                    pidigozzo_Random = random.randrange(1,10)
                    if(pidigozzo_Random == 1):
                        montepremi_vinto = montepremi_vinto + 10000
                        print("Hai vinto: 10000 €")
                    if(pidigozzo_Random == 2):
                        montepremi_vinto = montepremi_vinto + 15000
                        print("Hai vinto: 15000 €")
                    if(pidigozzo_Random == 3):
                        montepremi_vinto = montepremi_vinto + 20000
                        print("Hai vinto: 20000 €")
                    if(pidigozzo_Random == 4):
                        montepremi_vinto = montepremi_vinto + 25000 
                        print("Hai vinto: 25000 €")
                    if(pidigozzo_Random == 5):
                        montepremi_vinto = montepremi_vinto + 30000 
                        print("Hai vinto: 30000 €")
                    if(pidigozzo_Random == 6):
                        montepremi_vinto = montepremi_vinto + 40000 
                        print("Hai vinto: 40000 €")
                    if(pidigozzo_Random == 7):
                        montepremi_vinto = montepremi_vinto + 50000 
                        print("Hai vinto: 50000 €")
                    if(pidigozzo_Random == 8):
                        montepremi_vinto = montepremi_vinto + 75000
                        print("Hai vinto: 75000 €")
                    if(pidigozzo_Random == 9):
                        montepremi_vinto = montepremi_vinto + 150000 
                        print("Hai vinto: 150000 €")
                    print('Paolo Bonolis:"Il tuo montepremi attuale ammonta a"' , montepremi_vinto , '€')
                    tema_giocati = tema_giocati + 1
                    break
            if(risposta_minigioco == 1):
                break
        if(risposte_sbagliate_finale == 0):
            break
    if(risposte_sbagliate_finale == 0):
            break
    

    #primo tema (piante)
    while tema == 0:
        if(tema_1 == 1):
            break
        if(i == 0):
            print('Paolo Bonolis:"il tema delle domande che le verranno poste ora è sulle piante"')
            i = i + 1
        while risposte_sbagliate == 3:
            if(ciclo_finale == 0 ):
                print('Paolo Bonolis:"Il gioco è finito, Avanti un altro..."')
                print("Press any key to exit")
                ciclo_finale = ciclo_finale + 1
            else:
                continue
        domanda = random.randrange(0,5)
        if(domanda == 0):
            if(ripetizione_domanda_0 == 0):
                print('Paolo Bonolis:"La mimosa pudica è una delle piante più curiose al mondo, e deve il suo nome al fatto che è una timidona, cosa fanno le foglie di questa mimosa?"')
                print('Paolo Bonolis:"La risposta a è: "arrossiscono ai complimenti"')
                print('Paolo Bonolis:"La risposta b è: "si ritirano se le tocchi"')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                    ripetizione_domanda_0 = ripetizione_domanda_0 + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                    ripetizione_domanda_0 = ripetizione_domanda_0 + 1
            else:
                continue
        if(domanda == 1):
            if(ripetizione_domanda_1 == 0):
                print('Paolo Bonolis:"La più comune e iconica pianta carnivora dotata di una bocca dentata e definita da tanti una fra le più straordinarie è la?: "')
                print('Paolo Bonolis:"la risposta a è "Venere Acchiappamosche"')
                print('Paolo Bonolis:"la risposta b è "Dionaea Muscipola"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                    ripetizione_domanda_1 = ripetizione_domanda_1 + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                    ripetizione_domanda_1 = ripetizione_domanda_1 + 1
            else:
                continue
        if(domanda == 2):
            if(ripetizione_domanda_2 == 0):
                print('Paolo Bonolis:"Senza la luce avviene la germinazione?: "')
                print('Paolo Bonolis:"la risposta a è "Vero"')
                print('Paolo Bonolis:"la risposta b è "Falso"')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                    ripetizione_domanda_2 = ripetizione_domanda_2 + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                    ripetizione_domanda_2 = ripetizione_domanda_2 + 1
            else:
                continue
        if(domanda == 3):
            if(ripetizione_domanda_3 == 0):
                print('Paolo Bonolis:"Come si dividono le piante?: "')
                print('Paolo Bonolis:"la risposta a è "piante semplici e complesse"')
                print('Paolo Bonolis:"la risposta b è "piante vecchie e nuove"')
                print('Paolo Bonolis:"la risposta c è "piante grasse e succulente"')
                risposta = input('Paolo Bonolis:"Cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "C" or risposta == "c"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_3 = ripetizione_domanda_3 + 1
            else:
                continue
        if(domanda == 4):
            if(ripetizione_domanda_4 == 0):
                print('Paolo Bonolis:"Cosa sostiene le foglie?: "')
                print('Paolo Bonolis:"la risposta a è "radici"')
                print('Paolo Bonolis:"la risposta b è "rami"')
                print('Paolo Bonolis:"la risposta c è "fusto"')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "C" or risposta == "c"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1            
                ripetizione_domanda_4 = ripetizione_domanda_4 + 1
            else:
                continue
        while risposte_giuste == 3:
            print('Paolo Bonolis: "Complimenti ha superato il tema sulle piante, ora scelga un pidigozzo" ')
            print('Paolo Bonolis:"Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9"')
            pidigozzo_scelto = int(input('Paolo Bonolis:"Quale scegli?: "'))
            if(pidigozzo_scelto > 9):
                continue
            else:
                pidigozzo_Random = random.randrange(1,10)
                if(pidigozzo_Random == 1):
                    montepremi_vinto = montepremi_vinto + 10000
                    print("Hai vinto: 10000 €")
                if(pidigozzo_Random == 2):
                    montepremi_vinto = montepremi_vinto + 15000
                    print("Hai vinto: 15000 €")
                if(pidigozzo_Random == 3):
                    montepremi_vinto = montepremi_vinto + 20000
                    print("Hai vinto: 20000 €")
                if(pidigozzo_Random == 4):
                    montepremi_vinto = montepremi_vinto + 25000 
                    print("Hai vinto: 25000 €")
                if(pidigozzo_Random == 5):
                    montepremi_vinto = montepremi_vinto + 30000 
                    print("Hai vinto: 30000 €")
                if(pidigozzo_Random == 6):
                    montepremi_vinto = montepremi_vinto + 40000 
                    print("Hai vinto: 40000 €")
                if(pidigozzo_Random == 7):
                    montepremi_vinto = montepremi_vinto + 50000 
                    print("Hai vinto: 50000 €")
                if(pidigozzo_Random == 8):
                    montepremi_vinto = montepremi_vinto + 75000
                    print("Hai vinto: 75000 €")
                if(pidigozzo_Random == 9):
                    montepremi_vinto = montepremi_vinto + 150000 
                    print("Hai vinto: 150000 €")
                print('Paolo Bonolis:"Il tuo montepremi attuale ammonta a"' , montepremi_vinto , '€')
                ripetizione_domanda_0 = 1
                ripetizione_domanda_1 = 1
                ripetizione_domanda_2 = 1
                ripetizione_domanda_3 = 1
                ripetizione_domanda_4 = 1
                tema_giocati = tema_giocati + 1
                tema_1 = tema_1 + 1
                break


    #secondo tema (l'unione europea)
    while tema == 1:
        if(tema_2 == 1):
            break
        if(i == 0):
            print('''Paolo Bonolis: "il tema delle domande che le verranno poste ora è sull'Unione europea"''')
            i = i + 1
        while risposte_sbagliate == 3:
            if(ciclo_finale == 0 ):
                print('Paolo Bonolis:"Il gioco è finito, Avanti un altro..."')
                print("Press any key to exit")
                ciclo_finale = ciclo_finale + 1
            else:
                continue
        domanda = random.randrange(0,5)
        if(domanda == 0):
            if(ripetizione_domanda_0 == 0):
                print('Paolo Bonolis:"La bandiera europea è costituita da un cerchio di 12 stelle dorate su uno sfondo blu. cosa rappresentano le stelle?"')
                print('''Paolo Bonolis:La risposta a è: "Gli ideali di unità, solidarietà e armonia tra i popoli d'Europa"''')
                print('Paolo Bonolis:"La risposta b è: "il numero dei paesi membri"')
                print('Paolo Bonolis:"La risposta c è: "i 12 membri fondatori"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "C" or risposta == "c"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_0 = ripetizione_domanda_0 + 1
            else:
                continue
        if(domanda == 1):
            if(ripetizione_domanda_1 == 0):
                print('''Paolo Bonolis:"La carta dei diritti fondamentali dell'unione europea è stata proclamata nel: "''')
                print('Paolo Bonolis:"la risposta a è "1990"')
                print('Paolo Bonolis:"la risposta b è "2000"')
                print('Paolo Bonolis:"la risposta c è "1980"')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "C" or risposta == "c"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_1 = ripetizione_domanda_1 + 1
            else:
                continue
        if(domanda == 2):
            if(ripetizione_domanda_2 == 0):
                print('''Paolo Bonolis:"Il 25 marzo 2017 si sono celebrati i 60 anni dei Trattati di Roma, considerati l'atto di nascita dell'Unione Europea che, tuttavia, a quel tempo, non si chiamava ancora così. Qual era il nome della nascente organizzazione?"''')
                print('Paolo Bonolis:"la risposta a è "Comunità Economica Europea"')
                print('''Paolo Bonolis:"la risposta b è " Comunità europea del carbone e dell'acciaio"''')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_2 = ripetizione_domanda_2 + 1
            else:
                continue
        if(domanda == 3):
            if(ripetizione_domanda_3 == 0):
                print('Paolo Bonolis:"Il Trattato istitutivo della Cee prevedeva?"')
                print('Paolo Bonolis:"la risposta a è "La creazione di una moneta comune"')
                print('''Paolo Bonolis:"la risposta b è "L'eliminazione delle frontiere"''')
                print('Paolo Bonolis:"la risposta c è "La creazione di un mercato comune"')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "C" or risposta == "c"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1
                ripetizione_domanda_3 = ripetizione_domanda_3 + 1
            else:
                continue
        if(domanda == 4):
            if(ripetizione_domanda_4 == 0):
                print('Paolo Bonolis:"La sede della Banca Centrale Europea si trova a?"')
                print('Paolo Bonolis:"la risposta a è "Madrid"')
                print('Paolo Bonolis:"la risposta b è "Amsterdam"')
                print('Paolo Bonolis:"la risposta c è "Francoforte sul Meno"')
                risposta = input('Paolo Bonolis:"cosa scegli?: "')
                if(risposta == "A" or risposta == "a"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print('Paolo Bonolis:"La risposta è sbagliata!"')
                    risposte_sbagliate = risposte_sbagliate + 1 
                if(risposta == "C" or risposta == "c"):
                    print('Paolo Bonolis:"La risposta è giusta!"')
                    risposte_giuste = risposte_giuste + 1           
                ripetizione_domanda_4 = ripetizione_domanda_4 + 1
            else:
                continue
        while risposte_giuste == 3:
            print('''Paolo Bonolis: "Complimenti ha superato il tema sull'Unione europea', ora scelga un pidigozzo" ''')
            print('Paolo Bonolis:"Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9"')
            pidigozzo_scelto = int(input('Paolo Bonolis:"Quale scegli?: "'))
            if(pidigozzo_scelto > 9):
                continue
            else:
                pidigozzo_Random = random.randrange(1,10)
                if(pidigozzo_Random == 1):
                    montepremi_vinto = montepremi_vinto + 10000
                    print("Hai vinto: 10000 €")
                if(pidigozzo_Random == 2):
                    montepremi_vinto = montepremi_vinto + 15000
                    print("Hai vinto: 15000 €")
                if(pidigozzo_Random == 3):
                    montepremi_vinto = montepremi_vinto + 20000
                    print("Hai vinto: 20000 €")
                if(pidigozzo_Random == 4):
                    montepremi_vinto = montepremi_vinto + 25000 
                    print("Hai vinto: 25000 €")
                if(pidigozzo_Random == 5):
                    montepremi_vinto = montepremi_vinto + 30000 
                    print("Hai vinto: 30000 €")
                if(pidigozzo_Random == 6):
                    montepremi_vinto = montepremi_vinto + 40000 
                    print("Hai vinto: 40000 €")
                if(pidigozzo_Random == 7):
                    montepremi_vinto = montepremi_vinto + 50000 
                    print("Hai vinto: 50000 €")
                if(pidigozzo_Random == 8):
                    montepremi_vinto = montepremi_vinto + 75000
                    print("Hai vinto: 75000 €")
                if(pidigozzo_Random == 9):
                    montepremi_vinto = montepremi_vinto + 150000 
                    print("Hai vinto: 150000 €")
                print('Paolo Bonolis:"Il tuo montepremi attuale ammonta a"' , montepremi_vinto)
                ripetizione_domanda_0 = 1
                ripetizione_domanda_1 = 1
                ripetizione_domanda_2 = 1
                ripetizione_domanda_3 = 1
                ripetizione_domanda_4 = 1
                tema_giocati = tema_giocati + 1
                tema_2 = tema_2 + 1
                break
    if(tema_1 == 1):
        if(tema_2 == 1):
            break



#inizializzo le variabili per l'ultimo livello
domanda_iniziale : int = 0
vinto : int = 0
risposta_finale : str = ''
bonus : int = 0
risposta_gioco_finale : str = ''
introduzione : int = 0

#Gioco finale
while True:
    while True:
        if(risposte_sbagliate_finale == 0):
            break
        if(domanda_iniziale == 1):
            break
        risposta_iniziale = input('''Paolo Bonolis:"Benvenuto, sei pronto per l'ultimo livello" (digitare si se si vuole procedere)''')
        if(risposta_iniziale == "si" or risposta_iniziale == "Si"):
            domanda_iniziale = domanda_iniziale + 1
            break
        else:
            continue
    if(risposte_sbagliate_finale == 0):
            break
    while introduzione == 0:
        print('Paolo Bonolis:"Benvenuto al gioco finale, sei molto vicino al premio finale, dovrai rispondere a 21 domande"')
        print('''Paolo Bonolis:"c'è solo una regola... devi dare la risposta sbagliata"''')
        print('Paolo Bonolis:"esempio: domanda = quanto fa 2 + 2"')
        print('Paolo Bonolis:"la risposta a è 4"')
        print('Paolo Bonolis:"la risposta b è 3"')
        print('Paolo Bonolis:"la risposta giusta è la b"')
        print('Paolo Bonolis:"Hai 8 tentativi, alla quinta risposta sbagliata potrai decidere se attivare un bonus"')
        print('Paolo Bonolis:"il bonus dimezzerà il tuo montepremi"')
        print('Paolo Bonolis:"ma avrai 3 tentativi in più"')
        print('Paolo Bonolis:"Il tuo montepremi ora ammonta a "' , montepremi_vinto , "€")
        introduzione = introduzione + 1
    if(vinto == 1):
        break
    if(risposte_sbagliate_finale < 8):
        print('Paolo Bonolis:"Hai ancora "' , risposte_sbagliate_finale , " tentativi rimanenti")
    
    if(risposte_sbagliate_finale == 3):
        if(bonus == 0):
            risposta_finale = input('Paolo Bonolis:"vuoi usare il bonus?" ')
            if(risposta_finale == "si" or risposta_finale == "Si"):
                risposte_sbagliate_finale = 6
                montepremi_vinto = montepremi_vinto / 2
                bonus = bonus + 1
                print('Paolo Bonolis:"Il tuo montepremi ammonta a "' , montepremi_vinto , "€")
                continue
            else:
                if(risposta_finale == "no" or risposta_finale == "No"):
                    continue
        else:
            continue
    #domanda numero 1#
    print("Sfera ebbasta è un famoso cantante?")
    print('a = "Rock"')
    print('b = "Trap"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 2#
    print("quale parte dell'ago entra prima nel tessuto?")
    print('a = "cruna"')
    print('b = "punta"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 3#
    print("Dove si trova la capitaneria di porto?")
    print('a = "a terra"')
    print('b = "a bordo"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 4#
    print("Esiste lo squalo dalla pinna?")
    print('a = "gialla"')
    print('b = "bianca"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 5#
    print("Quando è cotta la pasta")
    print('a = "si cala"')
    print('b = "si scola"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 6#
    print("Nel gioco briscola, quale carta è un carico?")
    print('a = "il tre"')
    print('b = "il cavallo"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 7#
    print("in che anno sono nati i simpson?")
    print('a = "80"')
    print('b = "90"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 8#
    print("la mela cade dall'albero quando è?")
    print('a = "acerba"')
    print('b = "matura"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 9#
    print("nell'isola d'elba c'è il porto?")
    print('a = "smeraldo"')
    print('b = "azzurro"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 10#
    print("il talco assorbe le macchie di?")
    print('a = "olio"')
    print('b = "rossetto"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 11#
    print("in un detto cosa rende chi si vendica?")
    print('a = "pane"')
    print('b = "focaccia"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 12#
    print("i panni sporchi si lavano in?")
    print('a = "famiglia"')
    print('b = "piazza"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 13#
    print("l'equipaggio di una nave pirata è detto?")
    print('a = "battaglione"')
    print('b = "ciurma"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 14#
    print("cosa attraversa i passanti?")
    print('a = "bottone"')
    print('b = "cintura"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 15#
    print("le hawaii erano chiamate isole?")
    print('a = "hamburger"')
    print('b = "sandwich"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 16#
    print("cosa sa sbucciare una scimmia?")
    print('a = "banana"')
    print('b = "mela"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 17#
    print("il tavolo all'italiana è senza?")
    print('a = "sponde"')
    print('b = "buche"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 18#
    print("quale animale incontra il piccolo principe?")
    print('a = "lupo"')
    print('b = "volpe"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 19#
    print("si toglie il pigiama chi si è appena?")
    print('a = "svegliato"')
    print('b = "addormentato"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
    #domanda numero 20#
    print("Harry potter diventa invisibile grazie a un?")
    print('a = "mantello"')
    print('b = "cappello"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        print("è giusto")
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    #domanda numero 21#
    print("cosa è stato scritto prima?")
    print('a = "va pensiero"')
    print('b = "nessun dorma"')
    risposta_gioco_finale = input("Cosa scegli?: ")
    if(risposta_gioco_finale == "a" or risposta_gioco_finale == "A"):
        risposte_sbagliate_finale = risposte_sbagliate_finale - 1
        continue
    if(risposta_gioco_finale == "b" or risposta_gioco_finale == "B"):
        print("è giusto")
        vinto = vinto + 1
        continue
if(vinto == 1):
    print("!!!HAI VINTO!!!")
    print("Congratulazioni hai vinto un montepremi di " , montepremi_vinto , "€")
if(risposte_sbagliate_finale == 0):
    print("GAME OVER")
    print("Press any key to exit")