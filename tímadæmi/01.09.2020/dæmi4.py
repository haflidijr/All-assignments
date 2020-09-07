max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

total = 0
days_when_amount_acquired = 1

for i in range(0, max_days):
    total += 2 ** i

    if days_when_amount_acquired <= max_days:
        if target <= total:
            break

    days_when_amount_acquired += 1
else:
    days_when_amount_acquired -= 1

if days_when_amount_acquired <= max_days:
    if target > total:
        days_when_amount_acquired = 0
    
print('Days needed:',days_when_amount_acquired)