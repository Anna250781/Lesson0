class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.insert(0,args[0])
        return object.__new__(cls)

    def __init__(self, name, num):
        self.name = name
        self.number_of_floors = num

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        floor = int(new_floor)
        if floor > self.number_of_floors or floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, floor + 1):
            print(i)

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def __eq__(self, other:int):
        return self.number_of_floors == other

    def __lt__(self, other:int):
        return self.number_of_floors < other

    def __le__(self, other:int):
        return self.number_of_floors <= other

    def __gt__(self, other:int):
        return self.number_of_floors > other

    def _ge__(self, other:int):
        return self.number_of_floors >= other

    def __ne__(self, other:int):
        return self.number_of_floors != other

    def __add__(self, value:int):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors + value}"

    def __radd__(self, value:int):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors + value}"

    def __iadd__(self, value: int):#- работают так же как и __add__ (возвращают результат его вызова).
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors + value}"

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)