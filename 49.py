import math
def vatcalculator():
    VAT = 0.15
    price = int(input("Input price"))
    print("Including Vat",round((1-VAT)*price,2),"Excluding Vat",price)
vatcalculator()
