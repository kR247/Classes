from random import randint


class Animal:

    def __init__(self, speed):
        self.speed = speed
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        self._cords = [dx, dy, dz]
        if dz >= 0:
            Animal._cords = [self._cords[0] * self.speed, self._cords[1] * self.speed, self._cords[2] * self.speed]
        else:
            print("It's too deep, i can't dive :(")
        self._cords = Animal._cords

    def get_cords(self):
        print(f' X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        print(f"{self.sound}")


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords = (self._cords[0], self._cords[1], self._cords[2] - abs(dz))
        self.speed = self.speed / 2


class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal,):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


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
