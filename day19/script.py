import pprint

pp = pprint.PrettyPrinter(indent=4)
with open('day19/input.txt', 'r') as file:
    rules, messages = file.read().split('\n\n')
    messages = messages.split("\n")
    rules_dict = dict()
    for line in rules.split('\n'):
        k, rule = line.split(': ')
        if rule[0] == '"':
            rule = rule[1:-1]
        else:
            rule = [sequence.split(' ') if ' ' in sequence else [sequence]
                    for sequence in (rule.split(' | ') if ' | ' in rule else [rule])]
        rules_dict[k] = rule

    
pp.pprint(rules_dict)
def check_sequence(rules, sequence, message):
    if not sequence:
        yield message
    else:
        index, *sequence = sequence
        for message in run(rules, index, message):
            yield from check_sequence(rules, sequence, message)
            
def run_expand(rules, alt, message):
    for sequence in alt:
        yield from check_sequence(rules, sequence, message)
        
def run(rules, index, message):
    if isinstance(rules[index], list):
        yield from run_expand(rules, rules[index], message)
    else:
        if message and message[0] == rules[index]:
            yield message[1:]
            
def match(rules, message):
    return any(m == '' for m in run(rules, '0', message))

def solve(rules, messages):
    return sum(match(rules, m) for m in messages)

rules_dict_2 = {
    **rules_dict,
    '8': [['42'], ['42', '8']],
    '11': [['42', '31'], ['42', '11', '31']]
}
result_1 = solve(rules_dict, messages)
result_2 = solve(rules_dict_2, messages)
print(f'Result 1: {result_1}')
print(f'Result 2: {result_2}')