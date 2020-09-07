#variables are assumed to be of type int if nothing else is stated

top_num = int(input("What is the upper number for the range: "))

number = 2

while number <= top_num:
    #sum up the divisors
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1
    #classify the number based on its divisor sum
    if number == sum_of_divisors:
        print(number,"is perferct")
    elif number < sum_of_divisors:
        print(number,"is abundant")
    else:
        print(number,"is deficient")
    number += 1
