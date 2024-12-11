from random import randint


class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, *args, **kwargs):
        self._coords = None
        self.speed = None
        for arg in args:
            if isinstance(arg, (list, tuple)):
                self._coords = list(arg[:3])
            if isinstance(arg, (int, float)):
                self.speed = arg

        if self._coords is None:
            self._coords = kwargs.get('coords', [0, 0, 0])
        if self.speed is None:
            self.speed = kwargs.get('speed', 1)

    def get_coords(self):
        return f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}'

    def move(self, *args):
        if isinstance(args[0], (list, tuple)):
            delta = args[0]
        else:
            delta = args[:3]
        for i in range(3):
            if i < 2:
                self._coords[i] += delta[i] * self.speed
            elif (z := delta[i] * self.speed) < 0:
                print(f"{z} meters, it's too deep, i can't dive :(")
            else:
                self._coords[i] += delta[i] * self.speed

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            return "Sorry, i'm peaceful :)"
        else:
            return "Be careful, i'm attacking you 0_0"

    def speak(self):
        return self.sound


class Bird(Animal):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beak = True

    def lay_eggs(self):
        return f'Here are(is) {randint(1, 4)} eggs for you'


class AqauticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dive_in(self, dz):
        self._coords[2] -= abs(dz) * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Duckbill(PoisonousAnimal, Bird, AqauticAnimal):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound = "Click-click-click"


if __name__ == "__main__":
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    print(db.speak())
    print(db.attack())
    db.move(1, 2, 3)
    print(db.get_coords())
    db.dive_in(6)
    print(db.get_coords())
    print(db.lay_eggs())
