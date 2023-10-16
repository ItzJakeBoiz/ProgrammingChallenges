import random
import math
def diceroll():
    result = {1:0,2:0,3:0,4:0,5:0,6:0}
    for x in range(100):
        result[random.randint(1,6)] += 1
    for x in result:
        y = result[x]
        final = ""
        fives = math.floor(y/5)
        final += "V"*fives
        final+= '|' *(y-(fives*5))
        print(str(x) + " = "+final)
diceroll()