#Calcola le tasse da pagare e stampa il risultato.
#Se hai guadagnato meno di 10.000€ all'anno paghi 0€ di irpef.
#Se hai guadagnato tra 10.000 e 30.000€ all'anno paghi il 22% di tasse.
#Se hai guadagnato più di 30.000 euro paghi il 22% da 10.000 fino a 30.000 euro più il 33% della somma eccedente.
guadagno = int(input("Quanto hai guadagnato quest'anno? "))
tassa = 0
tassa1 = 0
tassa2 = 0
if(guadagno < 10000):
    print("Non devi pagare le tasse ")
if(10000 < guadagno < 30000):
    tassa = (guadagno / 100 * 22)
    print("Dovrai pagare " , tassa , "€ di tasse")
if(guadagno > 30000):
    tassa1 = (20000 / 100 * 22)
    tassa2 = (guadagno - 30000)
    tassa2 = (tassa2 / 100 * 33)
    tassa = tassa1 + tassa2
    print("Dovrai pagare " , tassa , "€ di tasse")