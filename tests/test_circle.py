from src.Circle import Circle
import math


def test_circle_area_calculation():
    radius = 5
    circle = Circle(radius)
    assert circle.area == math.pi * (radius ** 2)


def test_circle_perimeter_calculation():
    radius = 10
    circle = Circle(radius)
    assert circle.perimeter == 2 * math.pi * radius


def test_circle_zero_area():
    radius = 0
    circle = Circle(radius)
    assert circle.area == 0


def test_circle_zero_perimeter():
    radius = 0
    circle = Circle(radius)
    assert circle.perimeter == 0

