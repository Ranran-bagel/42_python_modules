def ft_water_reminder():
    wa_inter = int(input("Days since last watering: "))
    if wa_inter > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
