low = int(input("Hvar byrjar bilið? "))
high = int(input("Hvar endar bilið? "))

summa_sléttra = 0

for number in range(low, high+1):
    if number % 2 == 0:
        summa_sléttra += number

print("Summan er:", summa_sléttra)