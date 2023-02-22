import random


#introduzione
while True:
    risposta_iniziale = input('Paolo Bonolis:"Benvenuto, desideri giocare ad avanti un altro?" ')
    if(risposta_iniziale == "si" or risposta_iniziale == "Si"):
        break
    else:
        continue


#inizializzo le variabili per il primo livello
montepremi_vinto = 0
tema_giocati = 0
tema_1 = 0
tema_2 = 0


#primo livello
print('Paolo Bonolis:"Benvenuto al primo livello..."')
while True:


    #Il pc sceglia il tema del gioco
    tema = random.randrange(0,2)


    #inizializzo le variabili del primo livello
    minigioco = 0
    domanda_minigioco = 0
    risposta = 0
    pidigozzo_Random = 0
    pidigozzo_scelto = 0
    risposta_minigioco = 0
    ripetizione_domanda_0 = 0
    ripetizione_domanda_1 = 0
    ripetizione_domanda_2 = 0
    ripetizione_domanda_3 = 0
    ripetizione_domanda_4 = 0
    i = 0
    risposte_sbagliate = 0
    risposte_giuste = 0
    ciclo_finale = 0

    #minigiochi
    while tema_giocati == 1:
        minigioco = random.randrange(0,4)
        while True:
            domanda_minigioco = random.randrange(0,2)
            print("!!!MINI GIOCO!!!")
            if(minigioco == 0):
                print('Paolo Bonolis:" Il personaggio che è appena entrato è... lo iettatore "')
                print('Paolo Bonolis:" Le regole sono semplici: se rispondi in modo corretto continui a giocare, se rispondi in modo errato, hai perso "')
                if(domanda_minigioco == 0):
                    print('''Lo iettatore:"La domanda è "Qual era il nome della ragazzina posseduta dal demonio ne L’esorcista?"''')
                    print('La risposta a è "Regan MacNeil"')
                    print('La risposta b è "Regan Mcneal"')
                    risposta = input("Cosa scegli?: ")
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai vinto!")
                        break
                    if(risposta == "b" or risposta == "B"):
                        print('Lo iettatore:"Il minigioco è finito... hai perso!"')
                if(domanda_minigioco == 1):
                    print('La domanda è "Quale capitolo della saga di venerdì 13 Jason inizia a usare la maschera da hockey?"')
                    print('La risposta a è "Venerdì 13 parte II- L’assassino ti siede accanto"')
                    print('La risposta b è "Venerdì 13 – Capitolo finale"')
                    risposta = input("Cosa scegli?: ")
                    if(risposta == "b" or risposta == "B"):
                        print("Il minigioco è finito... hai vinto!")
                        break
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai perso!")
                tema_giocati = tema_giocati + 1  
            if(minigioco == 1):
                print("Il personaggio che è appena entrato è La Regina del Web")
                print("Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso")
                if(domanda_minigioco == 0):
                    print('La domanda è "per cosa sta https?"')
                    print('La risposta a è "Hyper Text Transfer Protocol Secure"')
                    print('La risposta b è "HyperText Transfer Protocol"')
                    risposta = input("Cosa scegli?: ")
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai vinto!")
                        risposta_minigioco = risposta_minigioco + 1
                    if(risposta == "b" or risposta == "B"):
                        print("Il minigioco è finito... hai perso!")
                if(domanda_minigioco == 1):
                    print('La domanda è "in che anno è stato creato whatsapp"')
                    print('La risposta a è "2008"')
                    print('La risposta b è "2009"')
                    risposta = input("Cosa scegli?: ")
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai perso!")
                    if(risposta == "b" or risposta == "B"):
                        print("Il minigioco è finito... hai vinto!")
                        risposta_minigioco = risposta_minigioco + 1
                while risposta_minigioco == 1:
                    print('Paolo Bonolis: "Complimenti ha superato il minigioco, ora scelga un pidigozzo" ')
                    print("Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9")
                    pidigozzo_scelto = int(input("Quale scegli?: "))
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
            if(minigioco == 2):
                if(domanda_minigioco == 0):
                    print("Il personaggio che è appena entrato è L'Atleta totale italiano")
                    print("Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso")
                    print('la domanda è: "Quale numero di maglia indossava Lionel Messi al suo esordio con il Barca nel 2004?"')
                    print('La risposta a è "10"')
                    print('La risposta b è "7"')
                    print('La risposta c è "30"')
                    print('La risposta d è "5"')
                    risposta = input("Cosa scegli?: ")  
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai perso!")
                    if(risposta == "b" or risposta == "B"):
                        print("Il minigioco è finito... hai perso!")
                    if(risposta == "c" or risposta == "C"):
                        print("Il minigioco è finito... hai vinto!")
                        risposta_minigioco = risposta_minigioco + 1
                    if(risposta == "d" or risposta == "D"):
                        print("Il minigioco è finito... hai perso!")
                    if(domanda_minigioco == 1):
                        print("Il personaggio che è appena entrato è L'Atleta totale italiano")
                        print("Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso")
                        print('la domanda è: "Quale numero di maglia indossava Cristiano Ronaldo allo Sporting Lisbona?"')
                        print('La risposta a è "7"')
                        print('La risposta a è "11"')
                        print('La risposta a è "13"')
                        print('La risposta a è "28"')
                        risposta = input("Cosa scegli?: ")  
                        if(risposta == "a" or risposta == "A"):
                            print("Il minigioco è finito... hai perso!")
                        if(risposta == "b" or risposta == "B"):
                            print("Il minigioco è finito... hai perso!")
                        if(risposta == "c" or risposta == "C"):
                            print("Il minigioco è finito... hai perso!")
                        if(risposta == "d" or risposta == "D"):
                            print("Il minigioco è finito... hai vinto!")
                            risposta_minigioco = risposta_minigioco + 1
                while risposta_minigioco == 1:
                    print('Paolo Bonolis: "Complimenti ha superato il minigioco, ora scelga un pidigozzo" ')
                    print("Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9")
                    pidigozzo_scelto = int(input("Quale scegli?: "))
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
                        print("Il tuo montepremi attuale ammonta a" , montepremi_vinto)
                        tema_giocati = tema_giocati + 1 
                        break
                if(risposta_minigioco == 1):
                    break
            if(minigioco == 3):
                print("Il personaggio che è appena entrato è Lo Scienziato Pazzo")
                print("Le regole sono semplici: se rispondi in modo corretto peschi un pidigozzo, se rispondi in modo errato, hai perso")
                if(domanda_minigioco == 0):
                    print('La domanda è "in base a cosa sono ordinati gli elementi chimici della tavola periodica sono ordinati?"')
                    print('La risposta a è "secondo il valore crescente del numero atomico"')
                    print('La risposta b è "secondo il valore crescente della massa atomica"')
                    risposta = input("Cosa scegli?: ")
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai vinto!")
                        risposta_minigioco = risposta_minigioco + 1
                    if(risposta == "b" or risposta == "B"):
                        print("Il minigioco è finito... hai perso!")
                if(domanda_minigioco == 1):
                    print('La domanda è "il fosforo nella tavola periodica è rappresentato da"')
                    print('La risposta a è "Fs"')
                    print('La risposta b è "P"')
                    risposta = input("Cosa scegli?: ")
                    if(risposta == "b" or risposta == "B"):
                        print("Il minigioco è finito... hai vinto!")
                        risposta_minigioco = risposta_minigioco + 1
                    if(risposta == "a" or risposta == "A"):
                        print("Il minigioco è finito... hai perso!")
                while risposta_minigioco == 1:
                    print('Paolo Bonolis: "Complimenti ha superato il minigioco, ora scelga un pidigozzo" ')
                    print("Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9")
                    pidigozzo_scelto = int(input("Quale scegli?: "))
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
                        print("Il tuo montepremi attuale ammonta a" , montepremi_vinto)
                        tema_giocati = tema_giocati + 1
                        break
                break


    #primo tema (piante)
    while tema == 0:
        if(tema_1 == 1):
            break
        if(i == 0):
            print('Paolo Bonolis: "il tema delle domande che le verranno poste ora è sulle piante"')
            i = i + 1
        while risposte_sbagliate == 3:
            if(ciclo_finale == 0 ):
                print("Il gioco è finito, Avanti un altro...")
                print("Press any key to exit")
                ciclo_finale = ciclo_finale + 1
            else:
                continue
        domanda = random.randrange(0,5)
        if(domanda == 0):
            if(ripetizione_domanda_0 == 0):
                print("La mimosa pudica è una delle piante più curiose al mondo, e deve il suo nome al fatto che è una timidona, cosa fanno le foglie di questa mimosa?")
                print('La risposta a è: "arrossiscono ai complimenti"')
                print('La risposta b è: "si ritirano se le tocchi"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                ripetizione_domanda_0 = ripetizione_domanda_0 + 1
            else:
                continue
        if(domanda == 1):
            if(ripetizione_domanda_1 == 0):
                print("La più comune e iconica pianta carnivora dotata di una bocca dentata e definita da tanti una fra le più straordinarie è la?:")
                print('la risposta a è "Venere Acchiappamosche"')
                print('la risposta b è "Dionaea Muscipola"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_1 = ripetizione_domanda_1 + 1
            else:
                continue
        if(domanda == 2):
            if(ripetizione_domanda_2 == 0):
                print("Senza la luce avviene la germinazione?: ")
                print('la risposta a è "Vero"')
                print('la risposta b è "Falso"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                ripetizione_domanda_2 = ripetizione_domanda_2 + 1
            else:
                continue
        if(domanda == 3):
            if(ripetizione_domanda_3 == 0):
                print("Come si dividono le piante?: ")
                print('la risposta a è "piante semplici e complesse"')
                print('la risposta b è "piante vecchie e nuove"')
                print('la risposta c è "piante grasse e succulente"')
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
                ripetizione_domanda_3 = ripetizione_domanda_3 + 1
            else:
                continue
        if(domanda == 4):
            if(ripetizione_domanda_4 == 0):
                print("Cosa sostiene le foglie?: ")
                print('la risposta a è "radici"')
                print('la risposta b è "rami"')
                print('la risposta c è "fusto"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "C" or risposta == "c"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1            
                ripetizione_domanda_4 = ripetizione_domanda_4 + 1
            else:
                continue
        while risposte_giuste == 3:
            print('Paolo Bonolis: "Complimenti ha superato il tema sulle piante, ora scelga un pidigozzo" ')
            print("Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9")
            pidigozzo_scelto = int(input("Quale scegli?: "))
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
                print("Il tuo montepremi attuale ammonta a" , montepremi_vinto)
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
                print("Il gioco è finito, Avanti un altro...")
                print("Press any key to exit")
                ciclo_finale = ciclo_finale + 1
            else:
                continue
        domanda = random.randrange(0,5)
        if(domanda == 0):
            if(ripetizione_domanda_0 == 0):
                print("La bandiera europea è costituita da un cerchio di 12 stelle dorate su uno sfondo blu. cosa rappresentano le stelle?")
                print('''La risposta a è: "Gli ideali di unità, solidarietà e armonia tra i popoli d'Europa"''')
                print('La risposta b è: "il numero dei paesi membri"')
                print('La risposta c è: "i 12 membri fondatori"')
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
                print("La carta dei diritti fondamentali dell'unione europea è stata proclamata nel: ")
                print('la risposta a è "1990"')
                print('la risposta b è "2000"')
                print('la risposta c è "1980"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "C" or risposta == "c"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_1 = ripetizione_domanda_1 + 1
            else:
                continue
        if(domanda == 2):
            if(ripetizione_domanda_2 == 0):
                print(" Il 25 marzo 2017 si sono celebrati i 60 anni dei Trattati di Roma, considerati l'atto di nascita dell'Unione Europea che, tuttavia, a quel tempo, non si chiamava ancora così. Qual era il nome della nascente organizzazione? ")
                print('la risposta a è "Comunità Economica Europea"')
                print('''la risposta b è " Comunità europea del carbone e dell'acciaio"''')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                ripetizione_domanda_2 = ripetizione_domanda_2 + 1
            else:
                continue
        if(domanda == 3):
            if(ripetizione_domanda_3 == 0):
                print("Il Trattato istitutivo della Cee prevedeva?")
                print('la risposta a è "La creazione di una moneta comune"')
                print('''la risposta b è "L'eliminazione delle frontiere"''')
                print('la risposta c è "La creazione di un mercato comune"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "C" or risposta == "c"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1
                ripetizione_domanda_3 = ripetizione_domanda_3 + 1
            else:
                continue
        if(domanda == 4):
            if(ripetizione_domanda_4 == 0):
                print("La sede della Banca Centrale Europea si trova a?")
                print('la risposta a è "Madrid"')
                print('la risposta b è "Amsterdam"')
                print('la risposta c è "Francoforte sul Meno"')
                risposta = input("cosa scegli?: ")
                if(risposta == "A" or risposta == "a"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1
                if(risposta == "B" or risposta == "b"):
                    print("La risposta è sbagliata!")
                    risposte_sbagliate = risposte_sbagliate + 1 
                if(risposta == "C" or risposta == "c"):
                    print("La risposta è giusta!")
                    risposte_giuste = risposte_giuste + 1           
                ripetizione_domanda_4 = ripetizione_domanda_4 + 1
            else:
                continue
        while risposte_giuste == 3:
            print('''Paolo Bonolis: "Complimenti ha superato il tema sull'Unione europea', ora scelga un pidigozzo" ''')
            print("Scegli tra il pidigozzo 1, 2, 3, 4, 5, 6, 7, 8 e 9")
            pidigozzo_scelto = int(input("Quale scegli?: "))
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
                print("Il tuo montepremi attuale ammonta a" , montepremi_vinto)
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
domanda_iniziale = 0
risposte_sbagliate_finale = 8
vinto = 0
risposta_finale = ''
bonus = 0
risposta_gioco_finale = ''


#Gioco finale
print('Paolo Bonolis:"Benvenuto al gioco finale, sei molto vicino al premio finale, dovrai rispondere a 21 domande"')
print('''Paolo Bonolis:"c'è solo una regola... devi dare la risposta sbagliata"''')
print('Paolo Bonolis:"esempio: domanda = quanto fa 2 + 2"')
print('Paolo Bonolis:"la risposta a è 4"')
print('Paolo Bonolis:"la risposta b è 3"')
print('Paolo Bonolis:"la risposta giusta è la b"')
print('Paolo Bonolis:"Hai 8 tentativi, alla quinta risposta sbagliata potrai decidere se attivare un bonus"')
print('Paolo Bonolis:"il bonus dimezzerà il tuo montepremi"')
print('Paolo Bonolis:"ma avrai 3 tentativi in più"')
print("Il tuo montepremi ora ammonta a " , montepremi_vinto , "€")
while True:
    while True:
        if(domanda_iniziale == 1):
            break
        risposta_iniziale = input('''Paolo Bonolis:"Benvenuto, sei pronto per l'ultimo livello" ''')
        if(risposta_iniziale == "si" or risposta_iniziale == "Si"):
            domanda_iniziale = domanda_iniziale + 1
            break
        else:
            continue
    if(vinto == 1):
        break
    if(risposte_sbagliate_finale < 8):
        print("Hai ancora " , risposte_sbagliate_finale , " tentativi rimanenti")
    if(risposte_sbagliate_finale == 0):
        break
    if(risposte_sbagliate_finale == 3):
        if(bonus == 0):
            risposta_finale = input('Paolo Bonolis:"vuoi usare il bonus?" ')
            if(risposta_finale == "si" or risposta_finale == "Si"):
                risposte_sbagliate_finale = 6
                montepremi_vinto = montepremi_vinto / 2
                bonus = bonus + 1
                print("Il tuo montepremi ammonta a " , montepremi_vinto)
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