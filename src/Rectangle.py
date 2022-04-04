from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a, self.__b = a, b
        self.__area = a * b
        self.__perimeter = (a + b) * 2
        super().__init__('Прямоугольник', self.__area, self.__perimeter)
