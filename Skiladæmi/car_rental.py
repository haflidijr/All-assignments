print("Welcome to car rentals!")


rent_a_car = (input("Would you like to continue (y/n)? "))

#Ef viðkomandi vill leigja bíl þá setur hann inn "y" (string) fyrir "yes"  og fer í while lykkjuna
while rent_a_car == "y":
    type_of_deal = input("Customer code (b or d): ")
    #Hér er valið hvorn bíladílinn viðkomandi vill, setur inn strenginn "b" eða annað fyrir "d" gefur svo upp upplýsingar type(int)
    if type_of_deal == "b":
        rent_days = int(input("Number of days: "))
       
        odometer_start = int(input("Odometer reading at the start: "))
       
        odometer_end = int(input("Odometer reading at the end: "))
       
        miles_driven = odometer_end - odometer_start
        print("Miles driven:",miles_driven)
       
        base_fee = 40
       
        mile_fee = 0.25
        #Hér er reiknað út gjald fyrir bílinn út frá upplýsingum, svarið er type(float)
        amount_due = (rent_days * base_fee) + (mile_fee * miles_driven)
        amount_due = round(amount_due, 1)       
        print("Amount due:",amount_due)
        #Ef viðkomandi vill díl "d" þá fer hann hingað og gefur upp upplýsingar type(int) og fær verð í type(float)
    else:
        rent_days = int(input("Number of days: "))

        odometer_start = int(input("Odometer reading at the start: "))

        odometer_end = int(input("Odometer reading at the end: "))

        miles_driven = odometer_end - odometer_start
        print("Miles driven:",miles_driven)

        base_fee = 60
        miles_p_day = miles_driven / rent_days
       
        if miles_p_day > 100:
            miles_fee = (miles_p_day - 100) * rent_days * 0.25
        
        else:
            miles_fee = 0

        amount_due = (rent_days * base_fee) + miles_fee
        amount_due = round(amount_due, 1)
        print("Amount due:",amount_due)

    rent_a_car = input("Would you like to continue (y/n)? ") 




