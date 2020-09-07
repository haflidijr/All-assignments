low = int(input("Sláðu inn lægri heiltölu: "))
high = int(input("Sláðu inn hærri heiltölu: "))

for i in range(low, high+1):
    if i % 2 != 0:
        print(i)