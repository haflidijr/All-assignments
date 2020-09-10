multiplier = int(input("Input number to multiply: "))
times_multiplier = int(input("Input how often to multiply: "))

outcome = 0

for i in range(1, times_multiplier + 1):
    outcome = i * multiplier
    print(outcome)
