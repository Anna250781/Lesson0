calls = 0
def count_calls(calls):
  #  if   ?????????????
    calls += 1
    return calls


my_tuple = ()
def string_info(my_tuple):
    global calls
    line = input("Введите название овоща: ")
    count = len(line)
    my_tuple = (count, line.upper(), line.lower())
    count_calls(calls)
    print(my_tuple)



string = True
def is_contains(string):
    global calles
    list_to_search = ["Алиса", "Светлана", "Ирина", "Вероника", "Татьяна"]
    name = input("Введите женское имя: ")
    for i in list_to_search:
        i == i.lower()
        if i == name.lower():
            string = True
        else:
            string = False
    count_calls(calls)
    print(string)


string_info(my_tuple)
is_contains(string)
print(calls)


