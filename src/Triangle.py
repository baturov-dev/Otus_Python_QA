from Figure import Figure
from Square import Square


class Triangle(Figure):
    name = 'triangle figure'

    def __new__(cls, side_1, side_2, side_3):
        if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
            return object.__new__(cls)
        else:
            return None

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3


    @property
    def area(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        return (p * (p-self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5

    @property
    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


square = Square(10)
triangle = Triangle(5, 4, 8)
print(triangle.area)
print(triangle.perimeter)
print(triangle.add_area(square))