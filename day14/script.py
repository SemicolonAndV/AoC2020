import re
from itertools import product

with open('day14/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]
    
def get_bin(x, n=36):
    if 'X' in x:
        return x
    return format(int(x), 'b').zfill(n)

def newstr_appender(item1, item2, bit):
    return [x if y == bit else y for x, y in zip(item1, item2)]

mem_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
mask_pattern = re.compile(r'mask = ([\d\w]+)')
data_parsed = [list(mem_pattern.match(x).groups()) if mem_pattern.match(x) else [0, mask_pattern.match(x).group(1)] for x in data]
int_to_bin = list(map(lambda x: [x[0], get_bin(x[1])], data_parsed))

newdict = {}
for item in int_to_bin:
    if type(item[0]) == int:
        current_mask = item[1]
    elif type(item[0]) == str:
        newstr = newstr_appender(item[1], current_mask, 'X')
        newdict[item[0]] = int(''.join(newstr), 2)
        
memory = {}
for item in int_to_bin:
    if type(item[0]) == int:
        current_mask = item[1]
    elif type(item[0]) == str:
        conv = get_bin(item[0])
        newstr = newstr_appender(conv, current_mask, '0')

        possibilities = current_mask.count('X')
        num_of_lists = 2 ** possibilities
        lists_to_sum = [list(newstr) for _ in range(num_of_lists)]
        iters = list(product(['0', '1'], repeat=possibilities))
        for i in range(len(iters)):
            current, index = iters[i], 0
            for j in range(len(lists_to_sum[i])):
                if lists_to_sum[i][j] == 'X':
                    lists_to_sum[i][j] = current[index]
                    index += 1

        for f in [int(''.join(i), 2) for i in lists_to_sum]:
            memory[f] = int(item[1], 2)
        
print(f"Result 1: {sum(newdict.values())}\nResult 2: {sum(map(lambda x: int(x), memory.values()))}")
