from src.input_layer.parser import InputParser, InputError
from src.plateau_size import PlateauSize
from src.rover_position import RoverPosition
from src.enums import Instructions, CompassDirections, InputType
import pytest


def test_InputParser_parse_plateau_gets_plateau_size():
    input_text = '5 5'

    result = InputParser.parse_plateau(input_text)

    assert result == PlateauSize(5, 5)


def test_InputParser_parse_plateau_rejects_invalid_plateau():
    input_text = 'a 5'
    
    with pytest.raises(InputError):
        InputParser.parse_plateau(input_text)


def test_InputParser_parse_rover_gets_rover_position():
    input_text = '1 1 N'

    result = InputParser.parse_rover(input_text)

    assert result == RoverPosition(1, 1, CompassDirections.NORTH)


def test_InputParser_parse_rover_rejects_invalid_position():
    input_text = '2 2 B'

    with pytest.raises(InputError):
        InputParser.parse_rover(input_text)


def test_InputParser_parse_instruction_gets_simple_instruction():
    input_text = 'M'

    result = InputParser.parse_instruction(input_text)

    assert result == [Instructions.MOVE]


def test_InputParser_parse_instruction_gets_complex_instruction():
    input_text = 'LLMRM'

    result = InputParser.parse_instruction(input_text)

    assert result == [Instructions.LEFT, Instructions.LEFT, Instructions.MOVE, Instructions.RIGHT, Instructions.MOVE]


def test_InputParser_parse_instruction_is_case_insensitive():
    input_text = 'llmrm'

    result = InputParser.parse_instruction(input_text)

    assert result == [Instructions.LEFT, Instructions.LEFT, Instructions.MOVE, Instructions.RIGHT, Instructions.MOVE]


def test_InputParser_parse_instruction_sanitises_instruction():
    input_text = 'LLBMPORAAM'

    result = InputParser.parse_instruction(input_text)

    assert result == [Instructions.LEFT, Instructions.LEFT, Instructions.MOVE, Instructions.RIGHT, Instructions.MOVE]


def test_InputParser_parse_input_gets_plateau():
    input_text = '2 3'

    result = InputParser.parse_input(input_text)

    assert result[0] == InputType.PLATEAU


def test_InputParser_parse_input_gets_rover():
    input_text = '4 2 W'

    result = InputParser.parse_input(input_text)

    assert result[0] == InputType.ROVER


def test_InputParser_parse_input_gets_instruction():
    input_text = 'LLM'

    result = InputParser.parse_input(input_text)

    assert result[0] == InputType.INSTRUCTION


def test_InputParser_parse_input_given_random_string_gets_correct_instruction():
    input_text = 'Sam Bramham Butts' # MRMM

    result = InputParser.parse_input(input_text)

    assert result[0] == InputType.INSTRUCTION
    assert result[1] == [Instructions.MOVE, Instructions.RIGHT, Instructions.MOVE, Instructions.MOVE]