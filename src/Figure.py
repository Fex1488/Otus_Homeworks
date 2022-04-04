class Figure:
    def __init__(self, name, area, perimeter):
        self.__name = name
        self.__area = area
        self.__perimeter = perimeter

    def __str__(self):
        return f'{self.name}, площадь: {self.area}, периметр: {self.perimeter}'

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    def add_area(self, figure):
        if isinstance(figure, Figure):
            self.__area += figure.area
        else:
            raise ValueError("Передан неправильный класс")

        return self.area
