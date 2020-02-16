from direction import Directions
import utility

class Robot:
    """The class represents the Robot. The main parameters are 
        direction - This is the direction in which the Robot is facing and can move in if move command is called.
        x_pos - The current x position(0-Indexed) of the Robot on the table.
        y_pos - The current y position(0-Indexed) of the Robot on the table.
    
    Raises:
        ValueError: If invalid values are passed as parameters this exception is raised.
    
    """

    def __init__(self,tableRef,init_x=0,init_y=0,direction=Directions.NORTH):
        """The constructor of the Robot
        
        Arguments:
            tableRef {Table} -- The Table object on which the robot is kept.
        
        Keyword Arguments:
            init_x {int} -- The initial x position (0-indexed) of the Robot (default: {0})
            init_y {int} -- The initial y position (0-indexed) of the Robot (default: {0})
            direction {int} -- Valid values for this are Directions.NORTH,Directions.SOUTH,Directions.EAST,Directions.WEST (default: {Directions.NORTH})
        
        Raises:
            ValueError: in case the parameters passed are invalid or the position of the Robot is outside the table.
        """
        self._direction=Directions.NORTH
        self.direction=direction #validates the value       
        self._table=tableRef
        self._x_pos=utility.validateInteger(init_x)
        self._y_pos=utility.validateInteger(init_y)
        #to-do Add table check
        if 0>=init_x>self._table.count_x-1 or 0>=init_y>self._table.count_y-1 :
            raise ValueError(f"The robot is being placed out of the table. Cannot place the Robot")
        
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

    def turn(self,value):
        """Makes the Robot turn left or Right
        
        Arguments:
            value {int} -- Valid values are Directions.LEFT or Directions.RIGHT
        
        Raises:
            ValueError: In case the value is not Directions.LEFT or Directions.RIGHT
        """

        #validate parameter values 
        if value not in Directions.validTurns():
            raise ValueError(f"The values can be only from the Directions class. valid values are Directions.RIGHT and Directions.LEFT")
        directionsArr=Directions.validDirections()
        index=directionsArr.index(self.direction)
        self.direction=index+value

    def move(self):
        """Moves the Robot one step ahead in the direction it is facing. If the step will make the Robot fall off the table the Robot remains in their position.
        """

        if self.direction==Directions.NORTH:
            self.y_pos=self.y_pos+1

        if self.direction==Directions.EAST:
            self.x_pos=self.x_pos+1

        if self.direction==Directions.SOUTH:
            self.y_pos=self.y_pos-1

        if self.direction==Directions.WEST:
            self.x_pos=self.x_pos-1





