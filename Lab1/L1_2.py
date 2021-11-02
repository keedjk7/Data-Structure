print(" *** Wind classification ***")
wind_Speed = float(input("Enter wind speed (km/h) : "))
if wind_Speed >= 0 and wind_Speed < 52 :
    print("Wind classification is Breeze.")
elif wind_Speed >= 52 and wind_Speed <56 :
    print("Wind classification is Depression.")
elif wind_Speed >=56 and wind_Speed < 102 :
    print("Wind classification is Tropical Storm.")
elif wind_Speed >= 102 and wind_Speed < 209 :
    print("Wind classification is Typhoon.")
elif wind_Speed >= 209 :
    print("Wind classification is Super Typhoon.")