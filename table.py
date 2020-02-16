import utility

class Table:
    """The class that represents the table on which the Robot is kept.
  
    """

    def __init__(self,count_x=5,count_y=5):
        """The constructor
        
        Arguments:
            count_x {int} -- The number of squares on the table on the x-axis. (default=5)
            count_y {int} -- The number of squares on the table on the y-axis. (default=5)
        """
        self.count_x=utility.validateInteger(count_x)
        self.count_y=utility.validateInteger(count_y)

            
    
    #x,y are zero indexed positions 
    def isPositionValid(self,x,y):
        """Checks is the position x (0-indexed) and y (0-indexed) are valid on the table. 
        
        Arguments:
            x {int} -- The 0-indexed position in x-direction.
            y {int} -- The 0-indexed position in y-direction.
        
        Returns:
            boolean -- If the 0-indexed position of x and y are on the table returns True else False
        """
        x=utility.validateInteger(int(x))
        y=utility.validateInteger(int(y))
        return 0<=x<=self.count_x-1 and 0<=y<=self.count_y-1 

    
