#Stampa il seguente pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
i = 1
n = str(1)
a = 0
while i <= 5:
    i = i + 1
    print(n)
    a = n + " " + str(i)
    n = a