from collections import defaultdict

with open('day10/input.txt', 'r') as file:
    data = sorted([int(x.strip()) for x in file.readlines()])
    
data = [0] + data
data.append(data[-1] + 3)
jolt_1, jolt_3 = 0, 0
for i in range(len(data)):
    current = data[i - 1]
    if (data[i] - current) == 1:
        jolt_1 += 1
    elif (data[i] - current) == 3:
        jolt_3 += 1
        
jumps = [1, 2, 3]
routes = defaultdict(int) # default value is 0
routes[0] = 1
for i in data[1:]:
    routes[i] = sum([routes[i - j] for j in jumps])

print(f"Result 1: {jolt_1 * jolt_3}\nResult 2: {routes[data[-1]]}")