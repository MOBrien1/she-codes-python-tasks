#booleans
moths_in_house = True
mitch_is_home = False

if moths_in_house is True:
    print("Get the moths!")

if mitch_is_home is False:
    print("No threats detected.")

moths_in_house = True
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("HOOMAN! Help me get the moths!")

moths_in_house = False
mitch_is_home = False

if not moths_in_house and not mitch_is_home:
    print("No threats detected.")

moths_in_house = True
mitch_is_home = False

if moths_in_house and not mitch_is_home:
    print("Meooooooowwwwwww! Hissssssssss!")

moths_in_house = False
mitch_is_home = True

if not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")
