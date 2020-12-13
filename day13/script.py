with open('day13/input.txt', 'r') as file:
    timestamp = int(file.readline())
    data = str(file.readline()).split(',')
    
data_1 = [int(x) for x in data if x != 'x']
res = sorted([(x - timestamp % x, x) for x in data_1], key=lambda x: x[0])

data_2 = [(int(x), data.index(x)) for x in data if x != 'x']

superbus_time = data_2[0][0]
final_time = 0
for bus, remainder in  data_2[1:]:
    while (final_time + remainder) % bus != 0:
        final_time += superbus_time
    superbus_time *= bus
    
print(f"Result 1: {res[0][0] * res[0][1]}\nResult 2: {final_time}")
