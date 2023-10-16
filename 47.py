def wordcount(sentance):
    count = 1
    for x in range(len(sentance)):
        if sentance[x] == " ":
            count+=1
    return count
def voulcount(sentance):
    count = 1
    for x in range(len(sentance)):
        if sentance[x] == "a" or sentance[x] == "e" or sentance[x] == "i" or sentance[x] == "o" or sentance[x] == "u":
            count+=1
    return count
def main():
    print("Sentance analysis\n\nEnter a sentance then press enter")
    sentance = input()
    print("Your sentance consists of",wordcount(sentance),"words and",voulcount(sentance),"vouls")
main()