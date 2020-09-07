low = int(input("Skrifið lægri heiltölu: "))
high = int(input("Skrifið hærri heiltölu "))

counter = low

while counter <= high:
    if counter % 2 == 1:
        print(counter)
    counter += 1
    