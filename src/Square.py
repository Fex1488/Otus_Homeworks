from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        self.__a = a
        self.__area = a * a
        self.__perimeter = (a + a) * 2
        super().__init__('Квадрат', self.__area, self.__perimeter)

