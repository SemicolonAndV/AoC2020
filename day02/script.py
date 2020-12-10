import re
from collections import Counter

with open('day2/input.txt', 'r') as file:
    data = file.readlines()

counter_1, counter_2 = 0, 0
for line in data:
    conv = re.match(r'(\d+)-(\d+)\s(\w):\s(\w+)', line)
    pwd = conv.group(4)
    ct = Counter(pwd)
    if int(conv.group(1)) <= ct[conv.group(3)] <= int(conv.group(2)):
        counter_1 += 1
    try:
        if (pwd[int(conv.group(1)) - 1] == conv.group(3)) ^ (pwd[int(conv.group(2)) - 1] == conv.group(3)):
            counter_2 += 1
    except IndexError:
        pass
    
print(f'Result 1: {counter_1}')
print(f'Result 2: {counter_2}')
