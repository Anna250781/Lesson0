def get_multiplied_digits(numbers):
    str_number = str(numbers)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if len(str_number) <= 1 and int(str_number[-1]) == 0:
        return first + 1
    else:
        return first


result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(420)
print(result1)
print(result2)

