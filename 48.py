import math
def swapajacent():
    word = input("Input the message you want to encrypt/dycrypt")
    final = ""
    for x in range(len(word)):
        if x/2 == math.floor(x/2):
            final+= word[x+1]
            final+= word[x]
    print(final)
swapajacent()