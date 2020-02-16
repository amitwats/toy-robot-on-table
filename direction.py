
# class NORTH:pass
# class EAST:pass
# class SOUTH:pass
# class WEST:pass
import utility

class Directions:
    NORTH=0
    EAST=1
    SOUTH=2
    WEST=3
    RIGHT=1
    LEFT=-1

    def validTurns():
        return [Directions.RIGHT,Directions.LEFT]

    def validDirections():
        return [Directions.NORTH,Directions.EAST,Directions.SOUTH,Directions.WEST]

    def validDirectionNames():
        return ['NORTH','EAST','SOUTH','WEST']

    def validTurnNames():
        return ['LEFT','RIGHT']

    def getDirectinoName(val):
        val=utility.validateInteger(val)
        val=val%4
        dirDict={0:"NORTH",1:"EAST",2:"SOUTH",3:"WEST"}
        return dirDict[val]

    def getDirectionValue(val):
        val=str(val).upper()
        if val not in Directions.validDirectionNames():
            raise ValueError(f"Expecting value to be one of the following '{validDirectionNames()}' found {val}")
        dirDict={"NORTH":Directions.NORTH,"EAST":Directions.EAST,"SOUTH":Directions.SOUTH,"WEST":Directions.WEST}
        return dirDict[val]
