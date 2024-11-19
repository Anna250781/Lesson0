from pprint import pprint
class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weigth = weight
        self. category = category

    def __str__(self):
        return f"{self.name}, {self.weigth}, {self. category}"


class Shop:
    def __init__(self, __file_name = "products.txt"):
        self.__file_name = __file_name

    def add(self, *products:Product):
        for i in products:
            if str(i) not in  self.get_products():
                file = open(self.__file_name, "a")
                file.write(f"{i}\n")
                file.close()
            else:
                print(f'Продукт {i} уже есть в магазине')
        return i

    def get_products(self):
        file = open(self.__file_name, "r")
        return file.read()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
