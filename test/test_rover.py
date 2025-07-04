from src.rover import Rover
from src.rover_position import RoverPosition
from src.enums import CompassDirections, Instructions


def test_Rover_creation():
    test_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    assert test_rover.position == (0, 0)
    assert test_rover.facing == CompassDirections.NORTH


def test_Rover_moves():
    test_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    test_rover.move()
    test_rover.confirm_movement()

    assert test_rover.position == (0, 1)


def test_Rover_rotates():
    test_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    test_rover.rotate(Instructions.LEFT)

    assert test_rover.facing == CompassDirections.WEST


def test_Rover_move_is_cached():
    test_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    test_rover.move()

    assert test_rover.position == (0, 0)
    assert test_rover.new_position == (0, 1)