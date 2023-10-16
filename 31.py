def minibus():
    age = int(input("What is your age?"))
    licence = str(input("Do you have your drivers licence? (Y/N)"))
    if (age >=21) & (licence == "Y"):
        print("You can drive the minibus")
    else:
        print("You can't drive the minibus")
minibus()