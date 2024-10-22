class House:
    def __init__(self, name, num):
        self.name = name
        self.number_of_floors = num


    def go_to(self, new_floor):
        floor = int(new_floor)
        f = 0
        if floor > self.number_of_floors or  floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, floor + 1):
            if i >= 1:
                f = f + 1
                print(f)
        return f

    
    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

