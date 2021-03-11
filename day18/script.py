import re

class I(int):
    def __add__(self, other):
        return I(self.real + other.real)
    
    def __sub__(self, other):
        return I(self.real * other.real)
    
    __mul__ = __add__

with open('day18/input.txt', 'r') as file:
    data = file.read().replace('*', '-')
    
modified_data = re.sub(r"(\d+)", r"I(\1)", data).splitlines()
result_1 = sum(eval(expression) for expression in modified_data)
result_2 = sum(eval(expression.replace("+", "*")) for expression in modified_data)
print(f"Result 1: {result_1}")
print(f"Reuslt 2: {result_2}")