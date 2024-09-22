calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(line):
    count = len(line)
    my_tuple = (count, line.upper(), line.lower())
    print(my_tuple)
    count_calls()


def is_contains(name,  list_to_search):
    string = 0
    for i in list_to_search:
        if i.lower()== name.lower():
            string = True
        else:
            string = False
    count_calls()
    return string
    print(string)


string_info("Зима")
string_info("Информация")
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

