
kvedja = "Hallo heimur!"
ord = kvedja[0:5]
print(ord)
# nu faum vid stok fra og med 0 til en ekki med 5
print("---------------")
annadHvert = kvedja[::2]
print(annadHvert)
# nu faum vid annadhvert stak i kvedjunni
print("---------------")
annadHvertOfugt = kvedja[::-2]
print(annadHvertOfugt)
# nu faum vid annadhvert stak i kvedjunni nema i ofugri rod
print("---------------")
ennEinnStrengurinn = kvedja[0:5:2]
print(ennEinnStrengurinn)
# fra og med 0, til en ekki med 5 og annadhvert stak, ta faum vid
# stokin 0, 2 og 4 eda Hlo

print("---------------")
# athugid ad tessar "slice" adgerdir breyta ekki upprunalega strengnum, hann
# er obreyttur
print(kvedja)
