from collections import Counter

def init_seats():
    seats = {}
    for y, line in enumerate(data):
        for x, seat in enumerate(line):
            if seat == 'L':
                seats[(x, y)] = 'empty'
            else:
                seats[(x, y)] = 'floor'
    return seats

def proximity(grid, x, y, mode):
    if mode == 'adjacent':
        toler = 4
        neighbours = part_1[(x, y)]
    elif mode == 'horizon':
        toler = 5
        neighbours = part_2[(x, y)]
    count = 0
    for coord in neighbours:
        try:
            if grid[coord] == 'taken':
                count += 1
        except KeyError:
            pass
    if count >= toler and grid[x, y] == 'taken':
        return 'empty'
    elif count == 0 and grid[x, y] == 'empty':
        return 'taken'
    return grid[x, y]

def find_horizon(x_mode, y_mode, find_mode):
    modes = {'x+y+': (x_mode + 1, y_mode + 1),
             'x+y=': (x_mode + 1, y_mode),
             'x+y-': (x_mode + 1, y_mode - 1),
             'x=y+': (x_mode, y_mode + 1),
             'x=y-': (x_mode, y_mode - 1),
             'x-y+': (x_mode - 1, y_mode + 1),
             'x-y=': (x_mode - 1, y_mode),
             'x-y-': (x_mode - 1, y_mode - 1)
             }
    return modes[find_mode]

def adjacent_neighbours(grid):
    part_1 = {}
    for k in grid.keys():
        neighbours = [(k[0] - 1, k[1] - 1), (k[0], k[1] - 1), (k[0] - 1, k[1]), (k[0] + 1, k[1] + 1),
                    (k[0] - 1, k[1] + 1), (k[0], k[1] + 1), (k[0] + 1, k[1]), (k[0] + 1, k[1] - 1)]
        part_1[(k)] = neighbours
    return part_1

def horizon_neighbours(grid):
    part_2 = {}
    for k in grid.keys():
        neighbours = []
        modes = ['x+y+', 'x+y-', 'x+y=', 'x=y+', 'x=y-', 'x-y+', 'x-y=', 'x-y-']
        while len(neighbours) < 8:
            for mode in modes:
                temp_x, temp_y = find_horizon(k[0], k[1], mode)
                try:
                    while grid[temp_x, temp_y] == 'floor':
                        temp_x, temp_y = find_horizon(temp_x, temp_y, mode)
                except KeyError:
                    temp_x, temp_y = -1, -1
                neighbours.append((temp_x, temp_y))
        part_2[(k)] = neighbours
    return part_2

def solve_grid(grid, mode):
    # seats = init_seats()
    changed = True
    while changed:
        changed = False
        tmp = grid.copy()
        for k, v in grid.items():
            if v == 'floor':
                continue
            tmp[k] = proximity(grid, k[0], k[1], mode)
            if tmp[k] != v:
                changed = True
        grid = tmp
    return grid
    
with open('day11/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]
    
seats = init_seats()
part_1 = adjacent_neighbours(seats)
part_2 = horizon_neighbours(seats)

print(f"Result 1: {Counter(solve_grid(seats, 'adjacent').values())['taken']}")
    
print(f"Result 2: {Counter(solve_grid(seats, 'horizon').values())['taken']}")
