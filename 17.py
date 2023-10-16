def f2c():
    marks1 = int(input("How many marks did the student get (COMP1)?"))
    marks2 = int(input("How many marks did the student get (COMP1)?"))
    total = marks1 + marks2
    percent = int(((total/160)*1000//1 )/10)

    grade = None
    if percent >=80:
        grade = "A"
    elif percent >=70:
        grade = "B"
    elif percent >=60:
        grade="C"
    elif percent >=50:
        grade="D"
    elif percent >=40:
        grade = "E"
    else:
        grade = "U"
    
    print("The student got a total score of",total,"and a percentage of",percent,"and a grade",grade)
f2c()