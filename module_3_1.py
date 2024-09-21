calls = 0
def count_calls():
    return calls


my_tuple = ()
def string_info(my_tuple):
    line = input("Введите название овоща: ")
    count = len(line)
    my_tuple = (count, line.upper(), line.lower())
    global calls
    count_calls()
    print(my_tuple)
    calls += 1

string = True
def is_contains(string):
    list_to_search = ["Алиса", "Светлана", "Ирина", "Вероника", "Татьяна"]
    name = input("Введите женское имя: ")
    for i in list_to_search:
        i == i.lower()
        global calls
        count_calls()
        if i == name.lower():
            string = True
            calls += 1
        else:
            string = False
    calls += 1
    print(string)


string_info(my_tuple)
string_info(my_tuple)
is_contains(string)
print(calls)


