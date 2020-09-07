low = int(input("Hvar byrjar bilið: "))
high = int(input("Hvar endar bilið: "))

for tala in range(low, high+1, 1):
    if tala % 2 == 1:
        print(tala)
        