def passwordguess():
    pswd = None
    while pswd != "secret":
        pswd = input("Whats the password?")
    print("You are in!")
passwordguess()