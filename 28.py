def evenodd():
    num = int(input("Enter a number:"))
    num = num/2
    if float(num).is_integer():
        print("Even")
    else:
        print("Odd")
evenodd()