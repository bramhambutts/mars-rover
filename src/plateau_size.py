from src.rover_position import RoverPosition
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
        other_x = other.x if type(other) == RoverPosition else other[0]
        other_y = other.y if type(other) == RoverPosition else other[1]

        test_x = other_x <= self.__x and other_x >= 0
        test_y = other_y <= self.__y and other_y >= 0

        return test_x and test_y
    

    def __repr__(self):
        return f'<PlateauSize object: {self.__x} {self.__y}>'