import re

def check_bag(color):
    if 'shiny gold' in color:
        return True
    return any(check_bag(x) for _, x in bags[color])
    
def count_bag(color):
    if color not in bags:
        return 0
    return sum(int(amount) + int(amount) * count_bag(x) for amount, x in bags[color])
    
with open('day07/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]
    
bags, counter_1 = {}, 0
for line in data:
    head = re.match(r"^(\w+\s\w+)", line).group()
    bags[head] = re.findall(r"(\d)\s([a-z]+\s[a-z]+)", line)

for k in bags.keys():
    if k != 'shiny gold':
        counter_1 += check_bag(k)
print(f"Result 1: {counter_1}\nResult 2: {count_bag('shiny gold')}")