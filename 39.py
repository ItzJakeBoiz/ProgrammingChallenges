def arrays():
    names = []
    for x in range(4):
        y = input("What do you want to name array "+str(x+1)+"\n")
        names.append(y)
    [names[0]] = ["value1"]
    [names[1]] = ["value2"]
    [names[2]] = ["value3"]
    [names[3]] = ["value4"]
    print([names[0]],[names[1]],[names[2]],[names[3]])

arrays()