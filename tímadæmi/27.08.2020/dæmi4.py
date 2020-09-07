n = int(input("Input an int: "))

division = 1

while n / division != 1:
    if n % division == 0:
        print(division)
    division += 1

print(n)

    
    
    
