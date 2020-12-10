with open("day1/input.txt", 'r') as file:
    data = sorted([int(line.strip()) for line in file.readlines()])
    
for i in range(len(data) - 2):
    for j in range(i + 1, len(data) - 1):
        if data[i] + data[j] == 2020:
            adding = data[i] * data[j]
        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                multi = data[i] * data[j] * data[k]
    
print(f"Part 1: {adding}")
print(f"Part 2: {multi}")
