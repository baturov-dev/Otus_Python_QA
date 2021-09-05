from Figure import Figure


class Rectangle(Figure):
    name = 'rectangle figure'

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)


rectangle = Rectangle(5,8)
print(rectangle.area)
print(rectangle.perimeter)