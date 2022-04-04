import pytest
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle


@pytest.fixture
def normal_triangle():
    triangle = Triangle(a=13, b=14, c=15)
    yield triangle
    del triangle


@pytest.fixture
def normal_rectangle():
    rectangle = Rectangle(a=5, b=20)
    yield rectangle
    del rectangle


@pytest.fixture
def normal_square():
    square = Square(a=10)
    yield square
    del square


@pytest.fixture
def normal_circle():
    circle = Circle(r=15)
    yield circle
    del circle
