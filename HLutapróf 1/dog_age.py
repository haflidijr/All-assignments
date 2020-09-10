dog_age = int(input("Input dog's age: "))

human_age = 0

if 17 > dog_age > 0:
    
    if dog_age == 1:
        
        human_age = 15
        
        print("Human age:",human_age)
    
    elif dog_age == 2:
        
        human_age = 24
        
        print("Human age:",human_age)

    else:
        human_age = dog_age * 4 + 16

        print("Human age:",human_age) 
    
else:
    print("Invalid age")