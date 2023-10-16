def driving_age():
    age = int(input("How old are you? "))
    if age > 75:
        print("You need to renew your licence annually")
    elif age >= 66:
        print("You need to renew your licence periodically")
    elif age >= 17:
        print("You are old enough to drive")
    elif age >= 16:
        print("You can drive from this year")
    else:
        print("You are too young to drive")


driving_age()