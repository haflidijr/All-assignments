points_str = input("Enter points ahead: ")
points_ahead_int = int(points_str)
lead_calc_float = float(points_ahead_int - 3)

has_ball_str = input("Does the winning team have the ball (Yes or No)? ")

if has_ball_str == "Yes":
    lead_calc_float = lead_calc_float + 0.5
else:
    lead_calc_float = lead_calc_float - 0.5

if lead_calc_float < 0:
    lead_calc_float = 0

lead_calc_float = lead_calc_float ** 2

sec_remaining_int = int(input("Enter the seconds remaining: "))

if lead_calc_float > sec_remaining_int:
    print("lead is safe.")
else:
    print("lead is not safe.")