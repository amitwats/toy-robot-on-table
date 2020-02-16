
# class NORTH:pass
# class EAST:pass
# class SOUTH:pass
# class WEST:pass
import utility

class Directions:
    """This is a static class equivalent. All methods in class represent the direction in which a Robot can face or turn. 
        VALID directions are 
            NORTH
            EAST
            SOUTH
            WEST
            RIGHT
            LEFT

    Raises:
        ValueError: For values outside the valid range.
    
    """


    NORTH=0
    EAST=1
    SOUTH=2
    WEST=3
    RIGHT=1
    LEFT=-1

    def validTurns():
        """The list of valid turns a Robot can do aka. RIGHT,LEFT
        
        Returns:
            int[] -- Array of integers having valid values of turns
        """
        return [Directions.RIGHT,Directions.LEFT]

    def validDirections():
        """The list of valid directions Robot can face aka. NORTH,EAST,SOUTH,WEST
        
        Returns:
            int[] -- Array of integers having valid values of directions the Robot can face.
        """

        return [Directions.NORTH,Directions.EAST,Directions.SOUTH,Directions.WEST]

    def validDirectionNames():
        """The list of valid directions names the Robot can face aka. "NORTH","EAST","SOUTH","WEST"
        
        Returns:
            str[] -- Array of strings having valid values of directions the Robot can face.
        """

        return ['NORTH','EAST','SOUTH','WEST']

    def validTurnNames():
        """The list of valid turns the Robot can make aka. "LEFT","RIGHT"
        
        Returns:
            str[] -- Array of strings having valid values of directions the Robot can turn.
        """
        return ['LEFT','RIGHT']

    def getDirectinoName(val:int):
        """Takes a number as an input and returns the name of the direction the number represents.
        
        Arguments:
            val {int} -- A number representing the direction the Robot can face.
        
        Returns:
            str -- The name of the direction the number 'val' represents.
        """

        val=utility.validateInteger(val)
        val=val%4
        dirDict={0:"NORTH",1:"EAST",2:"SOUTH",3:"WEST"}
        return dirDict[val]

    def getDirectionValue(val:str):
        """Takes a string as an input and returns the number of the direction the string represents.
        
        Arguments:
            val {str} -- A string equivalent of the direction the Robot can face.
        
        Returns:
            int -- The number representing the direction the string 'val' represents.
        """
        val=str(val).upper()
        if val not in Directions.validDirectionNames():
            raise ValueError(f"Expecting value to be one of the following '{validDirectionNames()}' found {val}")
        dirDict={"NORTH":Directions.NORTH,"EAST":Directions.EAST,"SOUTH":Directions.SOUTH,"WEST":Directions.WEST}
        return dirDict[val]
