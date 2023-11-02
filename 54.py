def binarybooks():
    file = open("books.bin","wb")
    while True:
        new  = ("Insert new book? (y/n)")
        if new == "n": break
        title = input("Insert the tile")
        isbn = input("Insert the ISBN")
        price = input("Insert the price")
        year = int(input("Insert the year of publication"))
