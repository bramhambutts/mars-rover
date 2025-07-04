from src.rover_position import RoverPosition
import copy
    

class Rover:


    def __init__(self, position):
        self.__position = position
        self.__new_position = None
    

    @property
    def position(self):
        return self.__position.coordinate
    

    @property
    def new_position(self):
        if self.__new_position != None:
            return self.__new_position.coordinate
        else:
            return self.position
    

    @property
    def facing(self):
        return self.__position.direction
    

    def rotate(self, direction):
        self.__position.rotate(direction)

    
    def move(self):
        self.__new_position = self.__position.move()

    
    def confirm_movement(self):
        self.__position = copy.copy(self.__new_position)
        self.__new_position = None
    

    def __repr__(self):
        return f'<Rover object: {self.position[0]} {self.position[1]} {self.facing.value}>'