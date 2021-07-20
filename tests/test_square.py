from src.Square import Square


def test_square_area_calculation():
    square_side = 5
    square = Square(square_side)
    assert square.area == square_side ** 2


def test_square_perimeter_calculation():
    square_side = 10
    square = Square(square_side)
    assert square.perimeter == square_side * 4


def test_square_zero_area():
    square_side = 0
    square = Square(square_side)
    assert square.area == 0


def test_square_zero_perimeter():
    square_side = 0
    square = Square(square_side)
    assert square.perimeter == 0