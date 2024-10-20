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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)