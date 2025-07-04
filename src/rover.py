import copy


class RoverPosition:


    def __init__(self, x, y, direction):
        self.__x = x
        self.__y = y
        self.__direction = direction
    

    @property
    def x(self):
        return copy.copy(self.__x)


    @property
    def y(self):
        return copy.copy(self.__y)
    

    @property
    def direction(self):
        return copy.copy(self.__direction)
    

    def __eq__(self, other):
        test_x = self.__x == other.x
        test_y = self.__y == other.y
        test_dir = self.__direction == other.direction

        return test_x and test_y and test_dir
    

    def __repr__(self):
        return f'<RoverPosition object: {self.__x} {self.__y} {self.__direction.value}>'