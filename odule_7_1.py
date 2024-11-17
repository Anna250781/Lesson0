from pprint import pprint
class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weigth = weight
        self. category = category

    def __str__(self):
        return f"{self.name}, {self.weigth}, {self. category}"


class Shop:
    __file_name = "products.txt"
    def add(self, *products:Product):
        for i in Shop. __file_name:
            if i != products:
                file = open(self.__file_name, "a")
                file.write(Product. __str__(self)) #?????????
                file.close()
            else:
                print(f'Продукт {Product. __str__(self)} уже есть в магазине')
            return

    def get_products(self):
        file = open(self.__file_name, "r")
        file.read()
        file.close()
        return self.__file_name #file #f"{self.__file_name}"

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
