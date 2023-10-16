def factors():
    num = int(input("What factors do you want to list?"))
    amt = 0
    for x in range (num):
        x+=1
        if (num/x) == (num/x)//1:
            print(x,"is a factor.")
            amt+=1
    print("There is a total of",amt,"factors.")
factors()