def cathedraltowns():
    data = {"Canterbury":{"Population":45055,"County":"Kent"}}
    while True:
        userInput = input("Enther the name of the county ('no' to end)")
        if userInput == "no": break#
        print("Cathedral towns in",userInput)
        hit = False
        for x in data:
            if data[x]["County"] == userInput:
                print(x,"population",data[x]["Population"])
                hit = True
        if hit == False: print("No cathedral towns were found in",userInput)

cathedraltowns()