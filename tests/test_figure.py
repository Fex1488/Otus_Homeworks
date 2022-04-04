import pytest
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle


def test_create_triangle():
    Triangle(13, 14, 15)


def test_create_triangle1():
    with pytest.raises(AttributeError):
        Triangle(13, 14, 114)


def test_create_rectangle():
    Rectangle(2, 15)


def test_create_square():
    Square(13)


def test_create_circle():
    Circle(17)


def test_figure_area_triangle(normal_triangle):
    assert normal_triangle.area == 84


def test_figure_area_square(normal_square):
    assert normal_square.area == 100


def test_figure_area_rectangle(normal_rectangle):
    assert normal_rectangle.area == 100


def test_figure_area_circle(normal_circle):
    assert normal_circle.area == 706


def test_figure_perimeter_triangle(normal_triangle):
    assert normal_triangle.perimeter == 42


def test_figure_perimeter_square(normal_square):
    assert normal_square.perimeter == 40


def test_figure_perimeter_rectangle(normal_rectangle):
    assert normal_rectangle.perimeter == 50


def test_figure_perimeter_circle(normal_circle):
    assert normal_circle.perimeter == 94


def test_add_area_not_normal_triangle(normal_triangle):
    with pytest.raises(ValueError):
        normal_triangle.add_area(123)
        normal_triangle.add_area('123')


def test_add_area_not_normal_square(normal_square):
    with pytest.raises(ValueError):
        normal_square.add_area(123)
        normal_square.add_area('123')


def test_add_area_not_normal_circle(normal_circle):
    with pytest.raises(ValueError):
        normal_circle.add_area(123)
        normal_circle.add_area('123')


def test_add_area_not_normal_rectangle(normal_rectangle):
    with pytest.raises(ValueError):
        normal_rectangle.add_area(123)
        normal_rectangle.add_area('123')


def test_add_area_triangle(normal_triangle, normal_square):
    assert normal_triangle.add_area(normal_square) == 184


def test_add_area_square(normal_square, normal_circle):
    assert normal_square.add_area(normal_circle) == 806


def test_add_area_circle(normal_circle, normal_rectangle):
    assert normal_circle.add_area(normal_rectangle) == 806


def test_add_area_rectangle(normal_rectangle, normal_triangle):
    assert normal_rectangle.add_area(normal_triangle) == 184
