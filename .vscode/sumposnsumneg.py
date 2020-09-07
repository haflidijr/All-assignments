a = int(input("tala nr. 1: "))
b = int(input("tala nr. 2: "))
c = int(input("tala nr. 3: "))

summa_positive = 0
summa_negative = 0

if a < 0:
    summa_negative += a
else:
    summa_positive += a

if b < 0:
    summa_negative += b
else:
    summa_positive += b

if c < 0:
    summa_negative += c
else:
    summa_positive += c

print("Summa jákvæðra talna var: ", summa_positive)
print("Summa neikvæðra talna var: ", summa_negative)
