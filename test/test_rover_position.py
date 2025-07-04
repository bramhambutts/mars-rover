from src.rover import RoverPosition
from src.enums import CompassDirections


def test_RoverPosition_stores_values():
    test_position = RoverPosition(1, 2, CompassDirections.NORTH)

    assert test_position.x == 1
    assert test_position.y == 2
    assert test_position.direction == CompassDirections.NORTH


def test_RoverPosition_is_equal():
    test_position = RoverPosition(1, 2, CompassDirections.NORTH)
    equal_position = RoverPosition(1, 2, CompassDirections.NORTH)

    assert test_position == equal_position