def discount():
    discounts = [[10000,0.8],[5000,0.85],[2500,0.9],[1000,0.95],[0,1]]
    amount = int(input("Whats the transaction amount?"))
    for discount in discounts:
        if amount > discount[0]:
            print("Discounted price is",(amount*discount[1]))
            break

discount()