def storagecases():
    prices = {}
    for x in range(11):
        prices[x] = ((x*0.82)+3.5)
    while True:
        d = int(input("how many dividers u want"))
        print(prices[d])
        x = input("u want more? (y/n)")
        if x == "n":
            break
storagecases()