
with open("day12/input.txt", 'r') as file:
    data = [(x[0], int(x[1:].strip())) for x in file.readlines()]
    
directions = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
clockwise = ['N', 'E', 'S', 'W']

def part_1():
    current_pos = [0, 0]
    current_dir = 'E'
    for op in data:
        if op[0] in clockwise:
            current_pos = [x + y for x, y in zip(current_pos, list(map(lambda x: op[1] * x, directions[op[0]])))]
        elif op[0] == 'L':
            current_dir = clockwise[(clockwise.index(current_dir) - op[1] // 90) % 4]
        elif op[0] == 'R':
            current_dir = clockwise[(clockwise.index(current_dir) + op[1] // 90) % 4]
        else:
            current_pos = [x + y for x, y in zip(current_pos, list(map(lambda x: op[1] * x, directions[current_dir])))]
        
    return sum(list(map(abs, current_pos)))
        
def part_2():
    waypoint = [10, 1]
    current_pos = [0, 0]
    rotation = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for op in data:
        if op[0] in clockwise:
            waypoint = [x + y for x, y in zip(waypoint, list(map(lambda x: op[1] * x, directions[op[0]])))]
        elif op[0] == 'L':
            if op[1] == 180:
                waypoint = list(map(lambda x: -x, waypoint))
            else:
                waypoint =  [x*y for x, y in zip(waypoint[::-1], rotation[-(op[1] // 90) % 4])]
        elif op[0] == 'R':
            if op[1] == 180:
                waypoint = list(map(lambda x: -x, waypoint))
            else:
                waypoint =  [x*y for x, y in zip(waypoint[::-1], rotation[(op[1] // 90) % 4])]
        else:
            current_pos = [x + y for x, y in zip(current_pos, list(map(lambda x: op[1] * x, waypoint)))]
    return sum(list(map(abs, current_pos)))
    
print(f"Result 1: {part_1()}")
print(f"Result 2: {part_2()}")
