a = int(input("tala nr. 1: "))
b = int(input("tala nr. 2: "))
c = int(input("tala nr. 3: "))

hæsta_tala = a

if b > hæsta_tala:
    hæsta_tala = b

if c > hæsta_tala:
    hæsta_tala = c

print("Hæsta talan er:", hæsta_tala)
