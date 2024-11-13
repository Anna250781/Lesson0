import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0 #степень опасности
    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz):
        self._cords[0] = self._cords[0] + dx * self.speed
        self._cords[1] = self._cords[1] + dy * self.speed
        self._cords[2] = self._cords[2] + dz * self.speed
        if self._cords[2] < 0:
            self._cords[2] = 0
            print("It's too deep, i can't dive :(")
        return


    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
            return
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True #наличие клюва
    def lay_eggs(self):
        eggs = [1, 2 , 3, 4]
        number = random.choice(eggs)
        print(f"Here are(is) {number} eggs for you")
        return


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        depth_chang = abs(dz) * self.speed / 2
        new_z = self._cords[2] - depth_chang
        if new_z < 0:
            new_z = self._cords[2]
        return new_z

#- где dz изменение координаты z в _cords.Должен
    # изменять в отрицательную сторону координату z уменьшенную в 2 раза с учётом скорости.
    # С    каким    бы    знаком    не    был    передан    параметр    dz,
    # внутри    метода    используйте    его    значение    по    модулю(функция abs).

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):#Порядок наследования определите сами
    def __init__(self, speed, _cords = [0, 0, 0], sound = "Click-click-click"):
        super().__init__(speed, _cords)
        self.sound = sound

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()


    # True
    # True
    # Click - click - click
    # Be careful, i 'm attacking you 0_0
    # X: 10  Y: 20  Z: 30
    # X: 10  Y: 20  Z: 0
    # Here are( is) 3 eggs for you  # Число может быть другим (1-4)