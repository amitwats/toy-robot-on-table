
# class NORTH:pass
# class EAST:pass
# class SOUTH:pass
# class WEST:pass

class Directions:
    NORTH=0
    EAST=1
    SOUTH=2
    WEST=3
    RIGHT=1
    LEFT=-1

    def validTurns():
        return [Directions.RIGHT,Directions.LEFT]