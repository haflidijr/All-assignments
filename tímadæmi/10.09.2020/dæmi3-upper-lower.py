a_str = input("Input a string: ")

count_upper = 0
count_lower = 0

for i in range(len(a_str)):
    if a_str[i].isupper():

        count_upper += 1

    elif a_str[i].islower():

        count_lower += 1

print(count_lower)
print(count_upper)