from copy import deepcopy

with open('day8/input.txt', 'r') as file:
    data = [line.strip().split(' ') for line in file.readlines()]


index, result_1, result_2 = 0, 0, None
while not result_2:
    temp_data = deepcopy(data)
    unchanged = False
    if temp_data[index][0] == 'nop':
        temp_data[index][0] = 'jmp'
    elif temp_data[index][0] == 'jmp':
        temp_data[index][0] = 'nop'
    else:
        unchanged = True
    previous_nums, curr_num, accumulator = [], 0, 0
    while True:
        try:
            if curr_num == len(temp_data):
                result_2 = accumulator
            if curr_num in previous_nums:
                if unchanged:
                    result_1 = accumulator
                break
            if temp_data[curr_num][0] == 'nop':
                previous_nums.append(curr_num)
                curr_num += 1
            elif temp_data[curr_num][0] == 'acc':
                previous_nums.append(curr_num)
                accumulator += int(temp_data[curr_num][1])
                curr_num += 1
            elif temp_data[curr_num][0] == 'jmp':
                previous_nums.append(curr_num)
                curr_num += int(temp_data[curr_num][1])
        except IndexError:
            break
    index += 1
print(f"Result 1: {result_1}\nResult 2: {result_2}")
