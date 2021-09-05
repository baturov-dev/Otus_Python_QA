from Figure import Figure


class Square(Figure):
    name = 'square figure'

    def __init__(self, square_side):
        self.square_side = square_side

    @property
    def area(self):
        return self.square_side ** 2

    @property
    def perimeter(self):
        return self.square_side * 4


square = Square(10)
print(square.area)
print(square.perimeter)



