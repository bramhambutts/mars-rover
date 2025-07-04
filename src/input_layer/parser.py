from src.enums import Instructions, CompassDirections, InputType
from src.plateau_size import PlateauSize
from src.rover_position import RoverPosition
import re


class InputError(Exception):
    pass


class InputParser:


    @staticmethod
    def parse_input(text):
        try:
            return [InputType.PLATEAU, InputParser.parse_plateau(text)]
        except InputError:
            try:
                return [InputType.ROVER, InputParser.parse_rover(text)]
            except InputError:
                return [InputType.INSTRUCTION, InputParser.parse_instruction(text)]


    @staticmethod
    def parse_plateau(text):
        positions = re.findall(r'\w+', text)
        if len(positions) != 2:
            raise InputError
        try:
            x = int(positions[0])
            y = int(positions[1])
            return PlateauSize(x, y)
        except ValueError:
            raise InputError('Could not find valid x or y')


    @staticmethod
    def parse_rover(text):
        parts = re.findall(r'\w+', text)

        if len(parts) != 3:
            raise InputError
        
        try:
            x = int(parts[0])
            y = int(parts[1])
            direction = CompassDirections(parts[2].upper())
            return RoverPosition(x, y, direction)
        except ValueError:
            raise InputError('Could not find valid components for position')


    @staticmethod
    def parse_instruction(text):
        possibles = [inst.value for inst in Instructions]
        instructables = re.findall(f'[{''.join(possibles)}]', text.upper())

        total_moves = [Instructions(instruction) for instruction in instructables]

        return total_moves