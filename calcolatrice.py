def somma(a, b):
    return a + b
def differenza(a, b):
    return a - b
def moltiplicazione(a, b):
    return a * b
def divisione(a, b):
    return a / b
while True:
    n1 : int = int(input("Inserisci un numero: "))
    n2 : int = int(input("Inserisci un numero: "))
    risposta : str = str(input("Scegli che operazione vuoi fare: "))
    if(risposta == "somma" or risposta == "Somma"):
        print(somma(n1, n2))
        break
    if(risposta == "differenza" or risposta == "Differenza"):
        print(differenza(n1, n2))
        break
    if(risposta == "moltiplicazione" or risposta == "Moltiplicazione"):
        print(moltiplicazione(n1, n2))
        break
    if(risposta == "divisione" or risposta == "Divisione"):
        if(n2 == 0):
            print("Non puoi dividere per 0")
            continue
        else:
            print(divisione(n1, n2))
            break
    