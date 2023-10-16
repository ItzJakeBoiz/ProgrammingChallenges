def loop():
    total = 0
    count = 0
    while True:
        number = int(input("Input the number\n"))
        total = total+number
        count = count+1
        if number == 999:
            print("Sum:",total,"\nCount:",count,"\nAverage:",(total/count))
            break
loop()