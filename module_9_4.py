first = 'Мама мыла раму'
second = 'Рамена мало было'
my_func = lambda x, y: x == y
my_list = list(map(lambda x, y: x == y, first, second))

print(my_list)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i)+"\n")
    return write_everything

write = get_advanced_writer('test.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random
class MysticBall:
    def __init__(self, *words):
        self.words = words


    def __call__(self, *words):
        a = random.choice(self.words)
        return a

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
