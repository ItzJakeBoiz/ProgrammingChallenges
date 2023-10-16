def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped: return
 
 
def sortnames():
    arr = []
    for x in range(10):
        arr.append(input("Enter name "+str(x+1)))
    bubbleSort(arr)
    for x in arr:
        print(x)
sortnames()