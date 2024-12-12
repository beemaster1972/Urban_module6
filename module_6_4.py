from math import pi


class Figure:
    sides_count = 0

    def __init__(self, *args, **kwargs):
        self.__sides = None
        self.filled = None
        self.__color = None
        sides = []
        for arg in args:
            if isinstance(arg, bool):
                self.filled = arg
                continue
            if isinstance(arg, (list, tuple)):
                if len(arg) == 3:
                    self.__color = list(arg) if self.__is_valid_color(arg) else None
                continue
            if isinstance(arg, int):
                sides.append(arg)
        if self.__color is None:
            self.__color = kwargs.get('color', [0, 0, 0])
        if self.filled is None:
            self.filled = kwargs.get('filled', False)
        if len(sides) != self.sides_count and len(sides) != 1:
            sides = [1] * self.sides_count
        elif len(sides) == 1:
            sides = sides * self.sides_count
        self.set_sides(*sides)

    @staticmethod
    def __is_valid_color(*colors):
        if len(colors) >= 3:
            colors = colors[:3]
        else:
            colors = colors[0]

        condition = [isinstance(color, int) and 0 <= color <= 255 for color in colors]
        return all(condition)

    def get_color(self):
        return self.__color

    def set_color(self, *color):
        if len(color) >= 3:
            color = color[:3]
        self.__color = color if self.__is_valid_color(color) else self.__color

    def __is_valid_sides(self, *args):
        condition = [isinstance(arg, int) and arg > 0 for arg in args[0]]
        return all(condition) and len(condition) == self.sides_count

    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    def __init__(self, *args, **kwargs):
        self.sides_count = 1
        super().__init__(*args, **kwargs)
        self.sides_count = 1
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure) :

    def __init__(self, *args, **kwargs):
        self.sides_count = 3
        super().__init__(*args, **kwargs)
        if super().get_sides() is None:
            del self


    def get_square(self):
        sides = self.get_sides()
        a, b, c = sides
        return pow((p := (sum(sides) / 2)) * (p - a) * (p - b) * (p - c), 1 / 2)

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            super().set_sides(*args)
            self.__sides = list(args)
        else:
            print(f'Нельзя построить треугольник со сторонами {args}')

    def __is_valid_sides(self, *args):
        if len(args) == 1:
            args = args[0]
        condition1 = [isinstance(arg, int) and arg > 0 for arg in args]
        condition = [args[0] < (args[1] + args[2]), args[1] < (args[0] + args[2]), args[2] < (args[0] + args[1])]
        return all(condition) and all(condition1)

    def __repr__(self):
        return f'Треугольник со сторонами {self.get_sides()}'


class Cube(Figure):
    def __init__(self, *args, **kwargs):
        self.sides_count = 12
        super().__init__(*args, **kwargs)
        self.__sides = [self.get_sides()[0]] * 12

    def get_volume(self):
        return self.__sides[0] * self.__sides[0] * self.__sides[0]


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # Проверка треугольника
    t1 = Triangle((0, 255, 0), 3, 4, 5, True)
    print(f'Площадь {t1} = {t1.get_square()}')
    print(f'Периметр {t1} = {len(t1)}')
    t2 = Triangle(12, 3, 4) # Не создастся
    t2 = Triangle(2, 3, 4)
    t2.set_sides(12,3,4)
    print(t2) # Не должны поменяться
