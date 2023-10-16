def timestable():
    table = int(input("What times table do you want?"))
    x = 0
    for x in range(1,11):
        
        print(x,"times",table,"=",(x*table))
        x +=1
timestable()