from src.enums import Instructions, CompassDirections
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
    

    @property
    def coordinate(self):
        return (self.__x, self.__y)
    

    def rotate(self, direction):
        direction_list = list(CompassDirections)
        current_index = direction_list.index(self.__direction)
        new_direction = None
        if direction == Instructions.LEFT:
            new_direction = direction_list[current_index-1]
        elif direction == Instructions.RIGHT:
            new_direction = direction_list[(current_index + 1) % len(direction_list)]
        return RoverPosition(*self.coordinate, new_direction)
    

    def move(self):
        new_x = copy.copy(self.__x)
        new_y = copy.copy(self.__y)
        if self.__direction == CompassDirections.NORTH:
            new_y = self.__y + 1
        elif self.__direction == CompassDirections.EAST:
            new_x = self.__x + 1
        elif self.__direction == CompassDirections.SOUTH:
            new_y = self.__y - 1
        elif self.__direction == CompassDirections.WEST:
            new_x = self.__x - 1
        return RoverPosition(new_x, new_y, copy.copy(self.__direction))


    def __eq__(self, other):
        if type(other) != RoverPosition:
            return False

        test_x = self.__x == other.x
        test_y = self.__y == other.y
        test_dir = self.__direction == other.direction

        return test_x and test_y and test_dir
    

    def __repr__(self):
        return f'<RoverPosition object: {self.__x} {self.__y} {self.__direction.value}>'