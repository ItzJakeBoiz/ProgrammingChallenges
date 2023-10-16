def inputdata():
    x = int(input("Input number 1 "))
    y = int(input("Input number 2 "))
    return [x,y]
def calculate_results(data):
    total = data[0] + data[1]
    avg = total/2
    return avg
def output_results(results):
    print("The average is",results)
def main():
    data = inputdata()
    output = calculate_results(data)
    output_results(output)
main()