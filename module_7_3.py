import io
import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            _word = []
            with open(str(i), "r", encoding = 'utf-8') as file:
                for line in file:
                    line = line.lower()
                    new_line = re.sub(r'[^\w\s]', '', line)
                    _word.extend(new_line.split())
                all_words[i] = _word
            return all_words

    def find(self, word):
        dict_1 = {}
        for key, value in self.get_all_words().items():
            num = 0
            for i in value:
                if word.lower() != i:
                    num = num + 1
                if word.lower() == i:
                    dict_1[key] = num + 1
                    return dict_1


    def count(self, word):
        dict_2 = {}
        for key, value in self.get_all_words().items():
            num_2 = 0
            for i in value:
                if word.lower()  == i:
                    num_2 = num_2 + 1
            dict_2[key] = num_2
            return dict_2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
