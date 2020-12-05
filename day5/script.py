conversion= ''.maketrans('FBRL', '0110')
f = lambda x: x[0] * 8 + x[1]
with open('day5/input.txt', 'r') as file:
    data = ([f([int(x.strip()[:7].translate(conversion), 2), int(x.strip()[7:].translate(conversion), 2)]) for x in file.readlines()])
empty_seats = {x for x in range(min(data), max(data))} - set(data)
print(f'Result 1: {max(data)}')
print(f'Result 2: {empty_seats}')
