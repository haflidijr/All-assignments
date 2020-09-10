a_str = input("Input a string: ")

chr_count = len(a_str)
word_count = 0

for i in a_str:

    if i == " ":
        word_count += 1
        chr_count -= 1
    elif i == "," or i == "." or i == "-":
        chr_count -= 1


print("No. of letters: {}, no. of words: {}".format(chr_count, word_count + 1))



