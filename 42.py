import math

def encrypt():
    msg = input("What do you want to encrypt?")
    length = len(msg)
    amount = math.ceil(length/6)
    arr = []
    count = 0
    for x in range(amount): arr.append([])
    for y in range(length):
        app = math.floor(y/6)
        if count >= length: 
            arr[app].append(" ")
        else:
            arr[app].append(msg[count])
        count+=1
    final = ""
    for x in range(6):
        for y in range(len(arr)):
            final += arr[y][x]
    print(final)
            
encrypt()
