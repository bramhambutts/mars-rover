from src.rover import Rover
from src.enums import Instructions, CompassDirections, InputType
import copy
import re


class ControlError(Exception):
    pass


class MissionControl:

    
    def __init__(self, plateau):
        self.__rovers = {}
        self.__plateau = plateau
        self.__current_rover = None
    

    @property
    def current_facing(self):
        if self.__current_rover != None:
            return self.__rovers[self.__current_rover].facing
        else:
            raise ControlError


    @property
    def current_position(self):
        if self.__current_rover != None:
            return self.__rovers[self.__current_rover].position
        else:
            raise ControlError


    @property
    def current_rover(self):
        return copy.copy(self.__current_rover)


    def get_rovers(self):
        return copy.deepcopy(self.__rovers)
    

    def get_size(self):
        return (self.__plateau.x, self.__plateau.y)

    
    def create_rover(self, rover):
        rover_names = self.__rovers.keys()
        highest_value = 0
        for name in rover_names:
            if re.findall(r'\ARover_', name) != []:
                number = int(re.findall(r'[0-9]+', name)[0])
                if number > highest_value:
                    highest_value = number
        
        new_name = f'Rover_{highest_value+1}'
        self.__rovers[new_name] = rover
        self.__current_rover = new_name


    def move_rover(self, movement):
        if self.__current_rover == None:
            raise ControlError
        
        current = self.__rovers[self.__current_rover]
        if movement == Instructions.MOVE:
            current.move()
            if current.new_position in self.__plateau:
                current.confirm_movement()
        else:
            current.rotate(movement)

    
    def switch_rover(self, rover_name):
        raise NotImplementedError