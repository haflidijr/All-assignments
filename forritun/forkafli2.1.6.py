numb = int(input("Krotaðu inn heiltölu vinur: "))
#Allar tölur eru type(int) nema annað sé tekið fram
divisor = 1
sum_of_divisors = 0

while divisor < numb:
    if numb % divisor == 0:
        sum_of_divisors = sum_of_divisors + divisor
    divisor = divisor + 1

if numb == sum_of_divisors:
    print(numb,"is perfect")
else:
    print(numb,"is not perfect")

