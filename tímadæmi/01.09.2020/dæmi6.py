length = int(input("Input the length of series: "))

the_sum = 0

for i in range(1, length+1):
    tala = i*2

    if i % 2 == 0:
        tala = -tala

    the_sum += tala
    print(tala)

print("Sum:", the_sum)
    
