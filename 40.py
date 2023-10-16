def array():
    table = []
    for x in range(8):
        name = input()
        marks = int(input())
        table.append([name,marks])
    for x in table:
        print(x[0],x[1])

array()