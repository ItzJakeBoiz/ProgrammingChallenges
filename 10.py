def gcseavg():
    amt = int(input("How many GCSE's did you take?"))
    total = 0
    for x in range(0,amt):
        total = total + int(input("What result did you get?"))
    print("Average : " + str(total/amt))
gcseavg()