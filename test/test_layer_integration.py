from src.input_layer.parser import InputParser
from src.mission_control import MissionControl, ControlError
from src.rover import Rover
import pytest


def test_move_single_rover():
    typer, new_plateau = InputParser.parse_input('5 5')
    mission = MissionControl(new_plateau)

    typer, rover_pos = InputParser.parse_input('1 2 N')
    new_rover = Rover(rover_pos)
    mission.create_rover(new_rover)

    typer, new_movement = InputParser.parse_input('LMLMLMLMM')
    for movement in new_movement:
        mission.move_rover(movement)

    assert repr(mission.get_rovers()['Rover_1']) == '<Rover object: 1 3 N>'
    

def test_move_multiple_rovers():
    typer, new_plateau = InputParser.parse_input('5 5')
    mission = MissionControl(new_plateau)

    typer, rover_pos = InputParser.parse_input('1 2 N')
    new_rover = Rover(rover_pos)
    mission.create_rover(new_rover)

    typer, new_movement = InputParser.parse_input('LMLMLMLMM')
    for movement in new_movement:
        mission.move_rover(movement)
    

    typer, rover_pos = InputParser.parse_input('3 3 E')
    new_rover = Rover(rover_pos)
    mission.create_rover(new_rover)

    typer, new_movement = InputParser.parse_input('MMRMMRMRRM')
    for movement in new_movement:
        mission.move_rover(movement)

    assert repr(mission.get_rovers()['Rover_1']) == '<Rover object: 1 3 N>'
    assert repr(mission.get_rovers()['Rover_2']) == '<Rover object: 5 1 E>'


def test_rover_returns_error_when_leaving():
    typer, new_plateau = InputParser.parse_input('5 5')
    mission = MissionControl(new_plateau)

    typer, rover_pos = InputParser.parse_input('1 2 N')
    new_rover = Rover(rover_pos)
    mission.create_rover(new_rover)
    
    typer, new_movement = InputParser.parse_input('LMM')
    for movement in new_movement:
        mission.move_rover(movement)

    assert repr(mission.get_rovers()['Rover_1']) == '<Rover object: 0 2 W>'


def test_rover_will_not_leave_plateau():
    typer, new_plateau = InputParser.parse_input('5 5')
    mission = MissionControl(new_plateau)

    typer, rover_pos = InputParser.parse_input('1 2 N')
    new_rover = Rover(rover_pos)
    mission.create_rover(new_rover)

    typer, new_movement = InputParser.parse_input('LMMMRMMMMMM')
    for movement in new_movement:
        mission.move_rover(movement)
    
    assert repr(mission.get_rovers()['Rover_1']) == '<Rover object: 0 5 N>'