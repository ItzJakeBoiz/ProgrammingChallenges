def moneydispenser():
    dispense = int(input("How much cash do you want to dispense?"))
    amounts =[[20,0],[10,0],[5,0],[2,0],[1,0]]
    x = 0
    while True:
        if x==5:
            break
        if (dispense- amounts[x][0]) >=0:
            dispense -= amounts[x][0]
            amounts[x][1] +=1
        else:
            x +=1
    x = 0
    while x in range(0,len(amounts)):
        print("£",amounts[x][0],"-",amounts[x][1])
        x+=1
            
moneydispenser()
