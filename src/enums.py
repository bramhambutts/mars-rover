from enum import Enum


class Instructions(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'


class CompassDirections(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'


class InputType(Enum):
    PLATEAU = 0
    ROVER = 1
    INSTRUCTION = 2