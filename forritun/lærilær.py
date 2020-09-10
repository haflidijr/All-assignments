my_str = input("Input a string: ")
index = 0
result = 'a' 

while index < len(my_str)-1:
    if my_str[index] < my_str[index+1]:
        result = result * 2
    else:
        result = result + my_str[index]
    index += 1
print(result)
