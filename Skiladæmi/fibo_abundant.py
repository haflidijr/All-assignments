choose_algorithm = input("Input f|a|b (fibonacci, abundant or both): ")

# Fibonacci sequence is a sequence of numbers where you find the next one by summing the
# two numbers before and so on.

if choose_algorithm == "f":
    num = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")

    numb1 = 0
    numb2 = 1

    if num >= 2:
        for i in range(0, num):
            print(numb1)
            nextnumb = numb1 + numb2

            numb1 = numb2
            numb2 = nextnumb

# The algorithm for abundant numbers is to find all the numbers with the divisor = 0 in that number.
# And if the sum of all that numbers is higher than the original number, it´s called "abundant".

elif choose_algorithm == "a":

    abndnt_nmbr = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")

    for number in range(1, abndnt_nmbr + 1):
        total = 0
        for i in range(1, number):
            if number % i == 0:
                total += i
        if total > number:
                print(number)


                   
                    
elif choose_algorithm == "b":
    num = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")


    numb1 = 0
    numb2 = 1

    if num >= 2:
        for i in range(0, num):
            print(numb1)
            nextnumb = numb1 + numb2

            numb1 = numb2
            numb2 = nextnumb

    

                    
    abndnt_nmbr = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")

    for number in range(1, abndnt_nmbr + 1):
        total = 0
        for i in range(1, number):
            if number % i == 0:
                total += i
        if total > number:
            print(number)
            
                
             
        
            
    

