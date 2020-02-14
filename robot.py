from direction import Directions

class Robot:

    def __init__(self,init_x=0,init_y=0,direction=Directions.NORTH):
        self._direction=Directions.NORTH
        self.direction=direction #validates the value       
        self._x_pos=init_x
        self._y_pos=init_y

    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @property
    def direction(self):
        return self._direction

    # # to-do Write test cases for value <0 and >3
    # # to-do write test cases for values non numerical 
    # @x_pos.setter
    # def x_pos(self, x):
    #     self._x_pos = x




    # to-do Write test cases for value <0 and >3
    # to-do write test cases for values non numerical 
    @direction.setter
    def direction(self, value):
        self._direction = value%4

    # to-do write test cases for multiple right/left subsequent terms
    def turn(self,value):
        #validate parameter values 
        if value not in Directions.validTurns():
            raise ValueError(f"The values can be only from the Directions class. valid values are Directions.RIGHT and Directions.LEFT")

        self.direction=self.direction+value
    def move():
        
        if self.direction==Directions.NORTH
        if self.direction==Directions.EAST
        if self.direction==Directions.SOUTH
        if self.direction==Directions.WEST


    # @property
    # def NORTH(self):
    #     return self._north

    # @property
    # def EAST(self):
    #     return self._east

    # @property
    # def SOUTH(self):
    #     return self._south

    # @property
    # def WEST(self):
    #     return self._west

    # def getDirection(self):
    #     return self.direction




