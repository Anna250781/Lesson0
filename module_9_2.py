first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x or y: len(x) or len(y) for x in first_strings for y in second_strings if len(x) % 2 or len(y) % 2}
four_result = {y: len(y) for y in second_strings if len(y) % 2}
five_result = {x: len(x) for x in first_strings if len(x) % 2}
print(first_result)
print(second_result)
print(third_result)
print(four_result)
print(five_result)

# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}