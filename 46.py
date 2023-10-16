def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
def getnumber():
    return int(input("Input the number you want to find the factorial of "))
def output(x):
    print("The factorial is ",x)
def main():
    num = getnumber()
    ans = factorial(num)
    output(ans)
main()
