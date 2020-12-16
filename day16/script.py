import re

with open('day16/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines() if x.strip()]
    
field_pattern = r'(.+): (\d+)-(\d+) or (\d+)-(\d+)'
fields, my_ticket, nearby_tickets = {}, [], []
part_1_items, part_1_results = [], []
for i, line in enumerate(data):
    i += 1
    if line == 'your ticket:':
       break     
    parser = re.match(field_pattern, line)
    
    for i in range(2, 6):
        part_1_items.append(int(parser.group(i)))
    fields[parser.group(1)] = [[x for x in range(int(parser.group(2)), int(parser.group(3)) + 1)], [x for x in range(int(parser.group(4)), int(parser.group(5)) + 1)]]

minpart1, maxpart1 = min(part_1_items), max(part_1_items)
my_ticket = [int(x) for x in data[i].split(',')]
i += 2
for line in data[i:]:
    nearby_tickets.append([int(x) for x in line.split(',')])
    for value in nearby_tickets[-1]:
        if value < minpart1 or value > maxpart1:
            part_1_results.append(value)
            nearby_tickets.pop(-1)
            break

part_2_results, transposed = {}, list(map(list, zip(*nearby_tickets)))
for k, v in fields.items():
    part_2_results[k] = []
    for i, item in enumerate(transposed):
        if not (set(item) - set(v[0] + v[1])):
            part_2_results[k].append(i)
            
final_fields, i, result_2 = {}, 0, 1
for k, v in sorted(part_2_results.items(), key=lambda x: len(x[1])):
    x = v[0]
    if 'departure' in k:
        final_fields[k] = x
        result_2 *= my_ticket[x]
    for v in part_2_results.values():
        if x not in v:
            continue
        v.pop(v.index(x))

print(f"Result 1: {sum(part_1_results)}\nResult 2: {result_2}")
