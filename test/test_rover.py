from src.rover import Rover
from src.rover_position import RoverPosition
from src.enums import CompassDirections, Instructions
import pytest


@pytest.mark.describe("Testing the Rover is initiated correctly")
class TestRoverBasics:


    @pytest.mark.context("Initialisation")
    @pytest.mark.it("start with direction")
    @pytest.mark.parametrize('x,y,direction',[
        (0, 0,  CompassDirections.NORTH),
        (3, 2,  CompassDirections.EAST ),
        (1, 12, CompassDirections.SOUTH),
        (4, 3,  CompassDirections.WEST )
    ], ids=['north', 'east', 'south', 'west'])
    def test_Rover_creation(self, x, y, direction):
        test_rover = Rover(RoverPosition(x, y, direction))

        assert test_rover.position == (x, y)
        assert test_rover.facing == direction


    @pytest.mark.context("Caching")
    @pytest.mark.it("Correctly caches movement")
    def test_Rover_move_is_cached(self):
        test_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

        test_rover.cache_movement()

        assert test_rover.position == (0, 0)
        assert test_rover.new_position == (0, 1)


@pytest.mark.describe("Testing that Rover movement is correctly undertaken")
class TestRoverMovement:


    @pytest.mark.context("Rover.move() single step")
    @pytest.mark.it("moves in direction")
    @pytest.mark.parametrize('x_in,y_in,direction,x_out,y_out',[
        (0, 0, CompassDirections.NORTH, 0, 1),
        (2, 2, CompassDirections.EAST,  3, 2),
        (4, 4, CompassDirections.SOUTH, 4, 3),
        (9, 9, CompassDirections.WEST,  8, 9)
    ], ids=['north', 'east', 'south', 'west'])
    def test_Rover_moves_once(self, x_in, y_in, direction, x_out, y_out):
        test_rover = Rover(RoverPosition(x_in, y_in, direction))

        test_rover.cache_movement()
        test_rover.confirm_movement()

        assert test_rover.position == (x_out, y_out)

    
    @pytest.mark.context("Rover.move() multiple steps")
    @pytest.mark.it("moves in direction")
    @pytest.mark.parametrize('x_in,y_in,direction,steps,x_out,y_out', [
        (0, 0, CompassDirections.NORTH, 3, 0, 3),
        (2, 2, CompassDirections.EAST,  6, 8, 2),
        (4, 4, CompassDirections.SOUTH, 2, 4, 2),
        (9, 9, CompassDirections.WEST,  5, 4, 9)
    ], ids=['3 x north', '6 x east', '2 x south', '5 x west'])
    def test_Rover_moves_multiple(self, x_in, y_in, direction, steps, x_out, y_out):
        test_rover = Rover(RoverPosition(x_in, y_in, direction))

        for step in range(steps):
            test_rover.cache_movement()
            test_rover.confirm_movement()
        
        assert test_rover.position == (x_out, y_out)


    @pytest.mark.context("Rover.rotate() single step")
    @pytest.mark.it("starting and rotating")
    @pytest.mark.parametrize('start_direction,rot_direction,end_direction', [
        (CompassDirections.NORTH, Instructions.LEFT,  CompassDirections.WEST ),
        (CompassDirections.EAST,  Instructions.LEFT,  CompassDirections.NORTH),
        (CompassDirections.SOUTH, Instructions.LEFT,  CompassDirections.EAST ),
        (CompassDirections.WEST,  Instructions.LEFT,  CompassDirections.SOUTH),
        (CompassDirections.NORTH, Instructions.RIGHT, CompassDirections.EAST ),
        (CompassDirections.EAST,  Instructions.RIGHT, CompassDirections.SOUTH),
        (CompassDirections.SOUTH, Instructions.RIGHT, CompassDirections.WEST ),
        (CompassDirections.WEST,  Instructions.RIGHT, CompassDirections.NORTH)
    ], ids=['north, left', 'east, left', 'south, left', 'west, left',
            'north, right', 'east, right', 'south, right', 'west, right'])
    def test_Rover_rotates_once(self, start_direction, rot_direction, end_direction):
        test_rover = Rover(RoverPosition(0, 0, start_direction))

        test_rover.rotate(rot_direction)

        assert test_rover.facing == end_direction


    @pytest.mark.context("Rover.rotate() multiple steps")
    @pytest.mark.it("rotating through")
    @pytest.mark.parametrize('rotations,end_direction', [
        ('LL', CompassDirections.SOUTH),
        ('RR', CompassDirections.SOUTH),
        ('LR', CompassDirections.NORTH),
        ('RL', CompassDirections.NORTH),
        ('LLL', CompassDirections.EAST),
        ('LLLL', CompassDirections.NORTH),
        ('LLLLL', CompassDirections.WEST),
        ('LLRLLRR', CompassDirections.WEST)
    ], ids=['LL', 'RR', 'LR', 'RL', 'LLL', 'LLLL', 'LLLLL', 'LLRLLRR'])
    def test_Rover_rotates_multiple(self, rotations, end_direction):
        test_rover = Rover(RoverPosition(0, 0, CompassDirections.NORTH))

        for rotation in list(rotations):
            rotation = Instructions.LEFT if rotation == 'L' else Instructions.RIGHT
            test_rover.rotate(rotation)
        
        assert test_rover.facing == end_direction