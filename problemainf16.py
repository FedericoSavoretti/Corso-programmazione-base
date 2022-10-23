i = 0
max = -999999999999999999999999999999999999999999
min = 999999999999999999999999999999999999999999
while True:
    i = int(input("Inserisci un numero: "))
    if(i == 0):
        break
    if(i > max):
        max = i
    if(i < min):
        min = i
print("Il numero maggiore è " , max)
print("Il numero minore è " , min)