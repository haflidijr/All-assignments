
import random
number = random.randint(0, 100)

print("Hi - Lo number guessing game: between 0 and 100 inclusive.")
print()
guess = int(input("Guess a number: "))

while 0 <= guess <= 100:
    if guess > number:
        print("Guess is too high")
    elif guess < number:
        print("Guess is to low")
    else:
        print("You guessed it. The number was:",number)
        break
    guess = int(input("Guess again: "))
else:
    (print("You quit early, the number was:",number))
