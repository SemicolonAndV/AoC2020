import re

with open('day4/input.txt', 'r') as file:
    data = [dict({y[:3]: y[4:] for y in x.replace('\n', ' ').split(' ')})for x in file.read().split('\n\n')]
    
# print(data)
valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_byr = [1920, 2002]
valid_iyr = [2010, 2020]
valid_eyr = [2020, 2030]
valid_hgt = r'(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in'
valid_hcl = r'#[0-9a-f]{6}'
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_pid = r'[0-9]{9}'

counter_1, counter_2 = 0, 0
for passport in data:
    fields, vals = 0, 0
    for key in passport.keys():
        if key in valid_fields:
            vals += 1
    if vals >= 7:
        counter_1 += 1
    try:
        if valid_byr[0] <= int(passport['byr']) <= valid_byr[1]:
            fields += 1
        if valid_iyr[0] <= int(passport['iyr']) <= valid_iyr[1]:
            fields += 1
        if valid_eyr[0] <= int(passport['eyr']) <= valid_eyr[1]:
            fields += 1
        if re.match(valid_hgt, passport['hgt']):
            fields += 1
        if re.match(valid_hcl, passport['hcl']):
            fields += 1
        if passport['ecl'] in valid_ecl:
            fields += 1
        if re.match(valid_pid, passport['pid']) and len(passport['pid']) == 9:
            fields += 1
        if fields >= 7:
            counter_2 += 1
    except KeyError:
        continue
            
print(counter_1)
print(counter_2)
