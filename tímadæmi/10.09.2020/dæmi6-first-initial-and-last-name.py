name = input("Input a name: ")

first, last = name.split()

last = last[0]

first = first[0:-1]

print("{}. {}".format(last.capitalize(), first.capitalize()))

   



