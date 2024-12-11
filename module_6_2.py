class Vehicle:
    __COLOR_VARIANTS = ['red','blue','green','black','white']
    def __init__(self, owner:str,model:str,engine_power:int,color:str):
        self.owner:str = owner
        self.__model:str = model
        if isinstance(engine_power,(int, float)):
            self.__engine_power,color = engine_power,color
        else:
            self.__engine_power, self.__color = color, engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец:{self.owner}')

    def set_color(self,new_color:str):
        if not new_color.lower() in self.__COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {new_color}")
            return
        self.__color = new_color


class Sedan(Vehicle):
    pass


if __name__ == "__main__":
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()