from src.plateau import PlateauSize
from src.rover import RoverPosition
from src.enums import CompassDirections


def test_PlateauSize_stores_values():
    test_plateau = PlateauSize(2, 3)

    assert test_plateau.x == 2
    assert test_plateau.y == 3


def test_PlateauSize_is_uneditable():
    test_plateau = PlateauSize(2, 3)

    test_x = test_plateau.x
    test_x += 1

    assert test_plateau.x == 2


def test_PlateauSize_is_equal():
    test_plateau = PlateauSize(2, 3)
    equal_plateau = PlateauSize(2, 3)

    assert test_plateau == equal_plateau


def test_PlateauSize_detects_RoverPosition_in_true():
    test_plateau = PlateauSize(5, 5)
    test_rover = RoverPosition(2, 3, CompassDirections.NORTH)

    assert test_rover in test_plateau


def test_PlateauSize_detects_RoverPosition_in_false():
    test_plateau = PlateauSize(5, 5)
    test_rover = RoverPosition(6, 2, CompassDirections.NORTH)

    assert (test_rover in test_plateau) == False