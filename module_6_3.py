class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, *args, **kwargs):
        self._coords = None
        self.speed = None
        for arg in args:
            if isinstance(arg,(list,tuple)):
                self._coords = list(arg[:3])
            if isinstance(arg,(int,float)):
                self.speed = arg

        if self._coords is None:
            self._coords = kwargs.get('coords',[0,0,0])
        if self.speed is None:
            self.speed = kwargs.get('speed',1)

    def get_coords(self):
        return f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}'

    def move(self, *args):
        delta = args[:3]
        for i, coord in enumerate(self._coords):
            if i < 2:
                coord += delta[i]*self.speed
            elif z:= delta[i]*self.speed < 0:
                print(f"{z} meters, it's too deep, i can't dive :(")
            else:
                coord += delta[i]*self.speed


if __name__ == "__main__":
    a = Animal((10,10,0),speed=2)
    a.move([2,2,-1])
    print(a.get_coords())


