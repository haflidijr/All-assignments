low = int(input("Hvar byrjar bilið? "))
high = int(input("Hvar endar bilið? "))

counter = low
summa = 0

while counter <= high:
    summa += counter
    counter += 1

print("Summan er:", summa)
