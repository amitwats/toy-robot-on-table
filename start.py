from robot import Robot
import direction
from direction import Directions
import direction
import utility
from table import Table 
from rparser import Parser
import sys


def makeMovement(file,tablex=5,tabley=5):
    """The main method that codes the logic of interaction between
    the Parser, Table and Robot. It uses the Parser object to generate all commands.
    The Table object is then created and a Robot is places on it. After validations the 
    Robot responds according to the commands in the input file.
    
    Arguments:
        file {str} -- The complete path of the file that contains the commands.
        tablex {int} -- The number of squares on the table on the x-axis. (default=5)
        tabley {int} -- The number of squares on the table on the y-axis. (default=5)
    """

    
    parsr=Parser(file)
    valid,lineNo,message=parsr.isValid()
    if valid:
        tabl=Table(int(tablex),int(tabley))
        rob=Robot(tabl)
        commands=parsr.allCommands
        for x in commands:
            if x.name=="PLACE":
                errorFound=False
                errorMessage=[]
                if 0<=int(x.parameters[0])<=tabl.count_x:
                    rob.x_pos=int(x.parameters[0])
                else:
                    errorFound=True
                    errorMessage.append(f"Invalid placement of Robot in X direction of table. The value should be between 1 and {tabl.count_x}.")

                if 0<=int(x.parameters[1])<=tabl.count_y:
                    rob.y_pos=int(x.parameters[1])
                else:
                    errorFound=True
                    errorMessage.append(f"Invalid placement of Robot in Y direction of table.The value should be between 1 and {tabl.count_y}.")
                
                try:
                    rob.direction=Directions.getDirectionValue(x.parameters[2].strip())
                except:
                    errorFound=True
                    errorMessage.append(f"Invalid value of direction in which the Robot is facing found {x.parameters[2]}, should be a value in {Directions.validDirectionNames()}")
                
                if errorFound:
                    errorMerged='\n\t'.join(errorMessage) 
                    print(f"Issue found in the PLACE command. \n\t{errorMerged}")
                    exit(1)
            elif x.name=="MOVE":
                rob.move()
            elif x.name=="LEFT":
                rob.turn(Directions.LEFT)
            elif x.name=="RIGHT":
                rob.turn(Directions.RIGHT)
            elif x.name=="REPORT":
                print(f"{rob.x_pos},{rob.y_pos},{Directions.getDirectinoName(rob.direction)}")
    else:
        print(f"Incomplete or wrong format found check to following errors\n {message} ")


def main():
    """
        The main method that is the entry point of the program. It reads the arguments passed and takes the first argument
        as the complete path of the commands file. 
    """
    if len(sys.argv)!=2:
        print("Invalid arguments length. Usage \n\t start [name of input file]")
        exit()
    else:
        fileName=sys.argv[1]
    makeMovement(fileName)

