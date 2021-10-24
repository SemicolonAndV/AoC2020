from itertools import product

with open('day17/input.txt', 'r') as file:
    data = [[x for x in line] for line in file.read().split("\n")]

            
def solve(partone=True):
    
    current_iteration = set()
    for row, x in enumerate(data):
        for col, y in enumerate(x):
            if y == "#":
                current_iteration.add((row, col, 0, 0))
                
    for _ in range(6):
        new_iteration = set()
        check = set()
        
        for (x, y, z, w) in current_iteration:
            for (dx, dy, dz, dw) in product([-1, 0, 1], repeat=4):
                if w + dw == 0 or not partone:
                    check.add((x + dx, y + dy, z + dz, w + dw))
                    
        for (x, y, z, w) in check:
            counter = 0
            for (dx, dy, dz, dw) in product([-1, 0, 1], repeat=4):
                if (dx, dy, dz, dw) != (0, 0, 0, 0):
                    if (x + dx, y + dy, z + dz, w + dw) in current_iteration:
                        counter += 1
                        
            if (x, y, z, w) not in current_iteration and counter == 3:
                new_iteration.add((x, y, z, w))
            if (x, y, z, w) in current_iteration and counter in [2, 3]:
                new_iteration.add((x, y, z, w))
        
        current_iteration = new_iteration
        
    return len(current_iteration)

result_1 = solve()
result_2 = solve(False)

print(f"Result 1: {result_1}")
print(f"Reuslt 2: {result_2}")