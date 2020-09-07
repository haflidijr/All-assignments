days_str = input("Number of days after 9/25/09: ")
days_int = int(days_str)

dist_sun_miles = 16637000000
spd_mph = 38241
time_hr = days_int * 24

dist_miles = spd_mph * time_hr + dist_sun_miles
print("Miles from the sun:" ,dist_miles)

dist_km = dist_miles * 1.609344 
dist_km = round(dist_km)
print("Kilometers from the sun:" ,dist_km)

dist_au = dist_miles / 92955887.6 
dist_au = round(dist_au)
print("AU from the sun:" ,dist_au)








