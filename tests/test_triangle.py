from src.Triangle import Triangle


def test_triangle_area_calculation():
    side_1 = 5
    side_2 = 10
    side_3 = 12
    p = (side_1 + side_2 + side_3) / 2
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.area == (p * (p-side_1) * (p - side_2) * (p - side_3)) ** 0.5


def test_triangle_perimeter_calculation():
    side_1 = 6
    side_2 = 11
    side_3 = 14
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.perimeter == side_1 + side_2 + side_3


def test_isosceles_triangle_perimeter():
    side_1 = 5
    side_2 = 10
    side_3 = 10
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.perimeter == side_1 + 2 * side_2


def test_equilateral_triangle_perimeter():
    side_1 = 10
    side_2 = 10
    side_3 = 10
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.perimeter == 3 * side_1


def test_equilateral_triangle_area():
    side_1 = 10
    side_2 = 10
    side_3 = 10
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.area == (side_1 ** 2) * ((3 ** 0.5) / 4)


