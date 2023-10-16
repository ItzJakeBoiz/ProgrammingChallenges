def writefile():
    file = open("students.txt",'w')
    app = ""
    for x in range(10):
        app+= "," +input("Enter students name")
    file.write(app)
    file.close()
    print("Updated file")
writefile()