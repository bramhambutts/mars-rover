from src.rover_position import RoverPosition
from src.enums import CompassDirections, Instructions


def test_RoverPosition_stores_values():
    test_position = RoverPosition(1, 2, CompassDirections.NORTH)

    assert test_position.x == 1
    assert test_position.y == 2
    assert test_position.direction == CompassDirections.NORTH


def test_RoverPosition_is_equal():
    test_position = RoverPosition(1, 2, CompassDirections.NORTH)
    equal_position = RoverPosition(1, 2, CompassDirections.NORTH)

    assert test_position == equal_position


def test_RoverPosition_is_indeditable():
    test_position = RoverPosition(1, 2, CompassDirections.NORTH)
    
    test_x = test_position.x
    test_x += 1

    assert test_position.x == 1


def test_RoverPosition_rotate_left():
    test_position = RoverPosition(0, 0, CompassDirections.NORTH)
    expected_position = RoverPosition(0, 0, CompassDirections.WEST)

    test_position.rotate(Instructions.LEFT)

    assert test_position == expected_position


def test_RoverPosition_rotate_right():
    test_position = RoverPosition(0, 0, CompassDirections.NORTH)
    expected_position = RoverPosition(0, 0, CompassDirections.EAST)

    test_position.rotate(Instructions.RIGHT)

    assert test_position == expected_position


def test_RoverPosition_move():
    test_position = RoverPosition(0, 0, CompassDirections.NORTH)
    expected_position = RoverPosition(0, 1, CompassDirections.NORTH)

    new_position = test_position.move()

    assert new_position == expected_position


def test_RoverPosition_coordinate():
    test_position = RoverPosition(0, 0, CompassDirections.NORTH)

    assert test_position.coordinate == (0, 0)