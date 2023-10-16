def scores():
    students = []
    while len(students) != 5:
        name = input("What is the students name?")
        score = int(input("What is the student's score?"))
        students.append([name,score])
    topmark = [None,0]
    for student in students:
        if student[1] > topmark[1]:
            topmark = student

    print("The top mark student is",topmark[0],"with",topmark[1],"Marks")
scores()