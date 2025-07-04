from src.mission_control import MissionControl, ControlError
from src.enums import CompassDirections, Instructions
from src.plateau import Plateau
from src.plateau_size import PlateauSize
from src.rover import Rover
from src.rover_position import RoverPosition
import pytest


def test_MissionControl_get_size():
    test_mission = MissionControl(PlateauSize(5, 5))
    
    assert test_mission.get_size() == (5, 5)


def test_MissionControl_get_rovers():
    test_mission = MissionControl(PlateauSize(5, 5))

    assert test_mission.get_rovers() == {}


def test_MissionControl_get_current_rover():
    test_mission = MissionControl(PlateauSize(5, 5))

    assert test_mission.current_rover == None


def test_MissionControl_fails_when_getting_rover_that_doesnt_exist():
    test_mission = MissionControl(PlateauSize(5, 5))

    with pytest.raises(ControlError):
        test_mission.current_position


def test_MissionControl_create_rover():
    test_mission = MissionControl(PlateauSize(5, 5))
    expected_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    test_mission.create_rover(expected_rover)

    assert test_mission.get_rovers()['Rover_1'].position == expected_rover.position
    assert test_mission.current_rover == 'Rover_1'


def test_MissionControl_rotate_rover():
    test_mission = MissionControl(PlateauSize(5, 5))
    new_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))
    
    test_mission.create_rover(new_rover)
    test_mission.move_rover(Instructions.LEFT)

    assert test_mission.current_facing == CompassDirections.WEST


def test_MissionControl_move_rover():
    test_mission = MissionControl(PlateauSize(5, 5))
    new_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    test_mission.create_rover(new_rover)
    test_mission.move_rover(Instructions.MOVE)

    assert test_mission.current_position == (0, 1)


def test_MissionControl_move_rover_doesnt_move_past_limits():
    test_mission = MissionControl(PlateauSize(5, 5))
    new_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

    test_mission.create_rover(new_rover)
    test_mission.move_rover(Instructions.LEFT)
    test_mission.move_rover(Instructions.MOVE)

    assert test_mission.current_position == (0, 0)