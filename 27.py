def journeycalc():
    print("Start time:")
    hours1 = int(input("Hours: "))
    min1 = int(input("Mins: "))
    print("Journey Length:")
    hours2 = int(input("How many hours did it take?"))
    min2 = int(input("How many mins did it take?"))
    hours3 = hours1+hours2
    min3 = min1+min2
    if min3>=60:
        min3 -=60
        hours3 +=1
    if hours3 > 12:
        hours3 -=12
        hours3 = str(hours3)+" PM"
    else:
        hours3 = str(hours3)+ "AM"
    print("End time:\nHours:",hours3,"\nMins:",min3)
journeycalc()