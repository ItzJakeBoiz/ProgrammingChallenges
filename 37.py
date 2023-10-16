def table():
    print("Multiplication Table")
    length = (int(input("What do you want the table to go up to?")))+1
    spacecount = len(str(length*length))
    numcount = len(str(length))

    for y in range(1,length):
        timestable = ""

        for z in range(1,length):
            timestable += ' '*spacecount
            insert = ""
            ans = str(z*y)

            if len(ans) != spacecount:
                insert += ' '*(spacecount-len(ans))

            insert += str(z*y)
            timestable += insert
        print(timestable)
table()