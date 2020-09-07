
# Collect numbers from the input and sort them to find the largest integer.
# If the number is negative, then it won´t go through the algorithm.
#
# The algorithm takes a number and values if it´s negative or not, if it´s not negative
# then the algorithm checks if it´s larger than max_int and replaces max_int if so.

num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0

while num_int >= 0:
    
    if num_int > max_int:
        max_int = num_int
    
    num_int = int(input("Input a number: "))

    

print("The maximum is", max_int)    # Do not change this line