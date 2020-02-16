import utility

class Table:
    def __init__(self,count_x,count_y):
        self.count_x=utility.validateInteger(count_x)
        self.count_y=utility.validateInteger(count_y)

            
    
    #x,y are zero indexed positions 
    def isPositionValid(self,x,y):
        x=utility.validateInteger(int(x))
        y=utility.validateInteger(int(y))
        return 0<=x<=self.count_x-1 and 0<=y<=self.count_y-1 

    
