
texti = input("Sláðu inn texta. ")
val = int(input("Með hvaða millibili viltu sjá stafina? "))

nýr_texti = texti[::val]
print(nýr_texti)
