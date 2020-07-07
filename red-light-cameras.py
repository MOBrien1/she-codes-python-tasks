light_colour = "Red"
car_detected = False
if light_colour == "Red" and not car_detected:
    print("Do nothing.")
elif light_colour == "Red" and car_detected:
    print("Flash!")
elif light_colour == "Green" and not car_detected:
    print("Do nothing.")
elif light_colour == "Green" and car_detected:
    print("Do nothing.")
elif light_colour == "Amber" and not car_detected:
    print("Do nothing.")
elif light_colour = "Amber" and car_detected:
    print("Do nothing.")
else:
    print("Do nothing.")