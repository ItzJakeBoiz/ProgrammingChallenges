def tax():
    pay = int(input("Whats your pay?"))
    taxamt = pay*0.25
    total = pay-taxamt
    print("Gross Pay: "+str(pay))
    print("Tax: "+str(taxamt))
    print("Net Pay: "+str(total))
tax()