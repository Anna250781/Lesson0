first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x,y in zip(first, second) if len(x) != len(y))
second_result = (True if len(x) == len(y) else False for x, y in range(len(first), len(second)))

print(list(first_result))
print(list(second_result))

# [1, 2]
# [False, False, True]