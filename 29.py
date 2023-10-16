def splitgold():
    gold = int(input("How much gold do you have?"))
    pirates = int(input("How many pirates do you need to split it between?"))
    perpirate = (gold/pirates)//1
    excess = gold-(perpirate*pirates)
    print("Each pirate gets",perpirate,"Gold and the captain gets to keep",excess,"gold.")

splitgold()