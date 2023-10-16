import random
def guess():
    number = random.randint(0,100)
    x=0
    while x in range(0,5):
        x+=1
        print("Guess Number",x)
        guess =  int(input("Guess the number "))
        if guess == number:
            print("Well done you got it")
        elif x == 5:
            print("Better luck next time, the number was",number)
        elif number > guess:
            print("Too low")
        else:
            print("Too high")

guess()