def minmax():
    min = 999
    max = 999
    while True:
        num = int(input("Input a number"))
        if num ==  -1:
            break
        if num > max or max ==999:
            max = num
        elif num < min or min==999:
            min = num
    print("Min:",min,"Max:",max)
minmax()