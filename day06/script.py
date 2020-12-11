from collections import Counter
import string

with open('day06/input.txt', 'r') as file:
    single_answers = [x.split('\n') for x in file.read().split('\n\n')]
    
group_answers = [''.join([x for x in item]) for item in single_answers]
answers_1, answers_2 = 0, 0
for i, item in enumerate(group_answers):
    cnt = Counter(item)
    answers_1 += len(cnt)
    for char in string.ascii_lowercase:
        if cnt[char] == len(single_answers[i]):
            answers_2 += 1

print(f'Result 1: {answers_1}\nResult 2: {answers_2}')