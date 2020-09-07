
low = int(input("Hvar byrjar bilið? "))
high = int(input("Hvar endar bilið? "))

counter = low
summa = 0

while counter <= high:
    if counter & 2 == 0:
        counter +=1    

    summa += counter
    counter += 1

print("Summa talnanna er:", summa)
