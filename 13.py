def f2c():
    miles = int(input("How many miles did you travel?"))
    fuel = int(input("How many litres of fuel did you use?"))
    gallons = fuel/4.546092
    mpg = miles/gallons
    print(mpg)
f2c()