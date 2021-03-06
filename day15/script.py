with open('day15/input.txt', 'r') as file:
    data = [int(x) for x in file.read().split(',')]
numbers = {}
for i, x in enumerate(data, start=1):
    numbers[x] = i
    
index = len(data) + 1
currnum = 0
while index < 30000000:
    if currnum not in numbers:
        numbers[currnum] = index
        currnum = 0
        index += 1
    else:
        lastnum = numbers[currnum]
        numbers[currnum] = index
        currnum = index - lastnum
        index += 1
    if index == 2020:
        res1 = currnum

print(f"Result 1: {res1}\nResult 2: {currnum}")
