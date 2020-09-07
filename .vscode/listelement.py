my_list = []

size = int(input("Hvað viltu stórann lista? "))

for x in range(1, size+1):
    current = int(input("Sláðu inn næstu tölu. "))
    my_list.append(current)

print(my_list)
