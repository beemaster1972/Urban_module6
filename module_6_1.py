class Plant:
    edible = False
    name = None

    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

    def __repr__(self):
        return f'{self.name} {"съедобен" if self.edible else "не съедобен"}'


class Animal:
    alive = True
    fed = False
    name = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} {"живой" if self.alive else "мёртвый"}'

    def eat(self, food):
        pass

    def get_status(self):
        return f'{self.name} {"живой" if self.alive else "мёртвый"}, {"сытый" if self.fed else "голодный"}'

    def check_alive(self)-> bool:
        if not self.alive:
            print(f'{self} мертв, и не может есть')
            return False
        else:
            return True

    def check_edible(self, food:Plant)-> bool:
        if food.edible:
            print(f'{self} съел {food}')
        else:
            self.alive = False
            print(f'{self} не стал есть {food}, и умер')
        return food.edible



class Mammal(Animal):
    edible = True
    def eat(self, food:Plant):
        if not self.check_alive():
            return
        if not isinstance(food,Plant):
            print(f'{self} травоядное и не ест {food}. {self} погибло')
            self.alive =False
            return
        self.fed = self.check_edible(food)




class Predator(Animal):
    def eat(self, food: Animal):
        if not self.check_alive():
            return

        if isinstance(food, Plant):
            print(f'{self} хищник и не ест {food}')
            self.alive = False
            return
        food.alive = False
        self.fed = self.check_edible(food)


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, True)


if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1)
    print(a2)
    print(p1)
    print(p2)
    print(a2.get_status())
    a1.eat(p1)
    a2.eat(p2)
    print(a1.get_status())
    print(a2.get_status())
    a3 = Predator('Медведь Балу')
    a3.eat(a2)
    print(a3.get_status())
    print(a2.get_status())