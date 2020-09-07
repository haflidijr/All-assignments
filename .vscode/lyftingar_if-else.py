a = input("Nafn keppanda: ")
b = int(input("Þyngd í kg: "))

if b < 60:
    print("lightweight")
elif b >= 60 and b <= 90:
    print("middleweight")
else:
    print("heavyweight")
