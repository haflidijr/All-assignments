low = int(input("Skrifið lægri heiltölu: "))
high = int(input("Skrifið hærri heiltölu: "))

summa = 0

for number in range(low, high+1):
    summa += number

print("summan er", summa)


