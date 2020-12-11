from itertools import combinations
from collections import deque

with open('day09/input.txt', 'r') as file:
    data = [int(x.strip()) for x in file.readlines()]
    
preamble, i = 25, 0
tempdata = deque(data[i:preamble + i])

while True:
    comb = combinations(set(tempdata), 2)
    available = list(map(lambda x: sum(x), list(comb)))
    if data[preamble + i] not in available:
        lastind = i + preamble
        result_1 = data[lastind]
        break
    tempdata.popleft()
    tempdata.append(data[preamble + i])
    i += 1
    
deque_res = None

for i in range(2, lastind):
    contigous, j = deque(data[lastind-i:lastind]), 1
    while not deque_res:
        if (i + j) == lastind:
            break
        contigous.pop()
        contigous.appendleft(data[lastind-i-j])
        j += 1
        if sum(tempdata) == result_1:
            deque_res = contigous
    
print(f"Result 1: {result_1}\nResult 2: {min(deque_res) + max(deque_res)}")