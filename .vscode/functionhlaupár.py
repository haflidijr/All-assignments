def hlaupár(ártal):
    if ártal % 4 == 0:
        if ártal % 100 == 0 and ártal % 400 != 0:
            return False
        else:
            return True
    else:
        return False


ár = int(input("Sláðu inn ártal og ég skal finna út hvort það sé hlaupár eða ekki. "))
if hlaupár(ár):
    print("hlaupár. ")
else:
    print("ekki hlaupár. ")

    