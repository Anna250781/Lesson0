import io
class WordsFinder:
    def __init__(self, *file_names:list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        _word = []
        for i in self.file_names:
            with open(str(i), "a+", encoding = 'utf-8') as self.file_names:
                for line in i:
                    line.lower()
                    for char  in line:
                        if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            del char
                        _word.append(*line.split())
                        all_words[i] = _word
        return all_words

#     def find(self, word):
#         dict_1 = {}
#         self.get_all_words()
#         return dict_1
#          где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
#
#     def count(self, word):
#         dict_2 = {}
#         self.get_all_words()
#         return dict_2
#          где ключ - название файла, значение - количество слова word в списке слов этого файла.
#
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом
# словаря - item().

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
#print(finder2.find('TEXT')) # 3 слово по счёту
#print(finder2.count('teXT')) # 4 слова teXT в тексте всего


# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
