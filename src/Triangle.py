import math
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not self.__existence_check(a, b, c):
            raise AttributeError("Error a, b, c")
        super().__init__('Треугольник', self.__area, self.__perimeter)

    def __existence_check(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.__a, self.__b, self.__c = a, b, c
            self.__p = (self.__a + self.__b + self.__c) / 2
            self.__area = int(math.sqrt(self.__p * (self.__p - self.__a) * (self.__p - self.__b) * (self.__p - self.__c)))
            self.__perimeter = int(self.__a + self.__b + self.__c)
            return True
        return False
