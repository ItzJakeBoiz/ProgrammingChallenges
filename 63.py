def lengthencryption():
    user_input = input("What do you want to compress?")
    msg = ""
    for x in range(len(user_input)):
        if (user_input[x] != user_input[(x-1)] or x == 0) and x != len(user_input):
            count = 0
            for y in range(x,len(user_input)):
                if user_input[y] == user_input[x]:
                    count+=1
                else: break
            msg += user_input[x]+" "+str(count)+ " "
    print(msg)
lengthencryption()