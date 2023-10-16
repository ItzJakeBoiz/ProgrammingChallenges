def f2c():
    members = int(input("How many club members?"))
    capacity = int(input("What's the seating capacity?"))
    coaches = (members/capacity)//1
    passangers = members - (coaches*capacity)
    print("There will be "+str(int(coaches))+" full coaches")
    print("With an excess coach of " +str(int(passangers)) + " people")

f2c()