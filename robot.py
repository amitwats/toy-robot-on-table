from direction import Directions
import utility

class Robot:

    def __init__(self,tableRef,init_x=0,init_y=0,direction=Directions.NORTH):
        self._direction=Directions.NORTH
        self.direction=direction #validates the value       
        self._x_pos=init_x
        self._y_pos=init_y
        self._table=tableRef
        #to-do Add table check

        #to-do check if the init_x and init_y are on the table. If not throw Value exception

    @property
    def table(self):
        return self._table

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
    @x_pos.setter
    def x_pos(self, x):
        if self.table.isPositionValid(x,self.y_pos):
            self._x_pos = x


    # # to-do Write test cases for value <0 and >3
    # # to-do write test cases for values non numerical 
    @y_pos.setter
    def y_pos(self, y):
        if self.table.isPositionValid(self.x_pos,y):
            self._y_pos = y


    # to-do Write test cases for value <0 and >3
    # to-do write test cases for values non numerical 
    @direction.setter
    def direction(self, value):
        value=utility.validateInteger(int(value))
        self._direction = value%4

    # to-do write test cases for multiple right/left subsequent terms
    def turn(self,value):
        #validate parameter values 
        if value not in Directions.validTurns():
            raise ValueError(f"The values can be only from the Directions class. valid values are Directions.RIGHT and Directions.LEFT")
        directionsArr=Directions.validDirections()
        index=directionsArr.index(self.direction)
        self.direction=index+value

    def move(self):
        if self.direction==Directions.NORTH:
            self.y_pos=self.y_pos+1

        if self.direction==Directions.EAST:
            self.x_pos=self.x_pos+1

        if self.direction==Directions.SOUTH:
            self.y_pos=self.y_pos-1

        if self.direction==Directions.WEST:
            self.x_pos=self.x_pos-1





