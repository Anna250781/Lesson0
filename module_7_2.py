import io
def custom_write(file_name, strings:list):
    strings_positions = {}
    num_line = 0
    num = ()
    for i in strings:
        file = open(file_name, "a", encoding = "utf-8")
        num_line += 1
        num = (num_line, file.tell())
        file.write(f"{i}\n")
        strings_positions[num] = i
        file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')