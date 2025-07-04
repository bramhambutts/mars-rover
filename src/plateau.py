import copy


class PlateauSize:


    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    @property
    def x(self):
        return copy.copy(self.__x)
    

    @property
    def y(self):
        return copy.copy(self.__y)


    def __eq__(self, other):
        test_x = self.__x == other.x
        test_y = self.__y == other.y

        return test_x and test_y
    

    def __contains__(self, other):
        test_x = other.x <= self.__x
        test_y = other.y <= self.__y

        return test_x and test_y
    

    def __repr__(self):
        return f'<PlateauSize object: {self.__x} {self.__y}>'