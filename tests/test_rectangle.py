from src.Rectangle import Rectangle


def test_rectangle_area_calculation():
    side_a = 5
    side_b = 10
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.area == side_a * side_b


def test_rectangle_perimeter_calculation():
    side_a = 10
    side_b = 15
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.perimeter == 2 * (side_a + side_b)


def test_rectangle_zero_side_a_area():
    side_a = 0
    side_b = 5
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.area == 0


def test_rectangle_zero_side_b_area():
    side_a = 5
    side_b = 0
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.area == 0


def test_rectangle_zero_side_a_perimeter():
    side_a = 0
    side_b = 5
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.perimeter == 2 * side_b


def test_rectangle_zero_side_b_perimeter():
    side_a = 5
    side_b = 0
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.perimeter == 2 * side_a

def test_rectangle_zero_sides_perimeter():
    side_a = 0
    side_b = 0
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.perimeter == 0
