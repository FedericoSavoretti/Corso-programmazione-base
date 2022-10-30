#Stampa i primi 10 numeri con il cliclo while.
# Se sono pari stampa anche un punto escamativo vicino al numero. 1 - 2! - 3 - 4!
i = 0
while(i <= 10):
    if(i%2):
        output = i
    else:
        output = (str(i) + "!")
    i = i + 1
    print(output)