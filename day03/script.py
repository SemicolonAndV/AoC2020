import math

with open('day03/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]
    
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counter_total = []
for slope in slopes:
    pos = 0
    tree_counter_current = 0
    for line in data[::slope[1]]:
        if line[pos % len(line)] == '#':
            tree_counter_current += 1
        pos += slope[0]
    tree_counter_total.append(tree_counter_current)
    
print(f'Result 1: {tree_counter_total[1]}')
print(f'Result 2: {math.prod(tree_counter_total)}')