with open('day15/input.txt', 'r') as file:
    data = [int(x) for x in file.read().split(',')]
numbers = {}
for i, x in enumerate(data, start=1):
    numbers[x] = i
    
def find_number(turn):
    index = len(data) + 1
    currnum = 0
    while index < turn:
        if currnum not in numbers:
            numbers[currnum] = index
            currnum = 0
            index += 1
        else:
            lastnum = numbers[currnum]
            numbers[currnum] = index
            currnum = index - lastnum
            index += 1
    return currnum

print(f"Result 1: {find_number(2020)}\nResult 2: {find_number(30000000)}")