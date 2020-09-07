inches_str = input("How many inches of rain have fallen? ")
inches_int = int(inches_str)
acre_field = 43560
volume = (inches_int/12) * acre_field

gallons = volume * 7.48051945

print(inches_int, "in. rain on 1 acre is" ,gallons, "gallons")

