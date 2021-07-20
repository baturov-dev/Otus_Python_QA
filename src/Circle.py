from Figure import Figure
import math


class Circle(Figure):
    name = 'circle figure'

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(10)
print(circle.area)
print(circle.perimeter)