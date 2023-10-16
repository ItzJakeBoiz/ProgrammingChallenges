def namesort():
    names = []
    i = 0
    for i in range(0,3):
        i +=1
        name = input("Whats their name? ")
        names.append(name)
    names.sort()
    for name in names:
        print(name)
namesort()