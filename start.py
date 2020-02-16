from robot import Robot
import direction
from direction import Directions
import direction
import utility
from table import Table 
import click
from rparser import Parser
import sys


# def test_remainder():

#     for x in range(-10,10):
#         print(f"The remainder of {x}%4 is {x%4}")

# def test_turning_right():
#     r=Robot()
#     for x in range(10):
#         r.turn(Directions.RIGHT)
#         print(r.direction)

# def test_turning_left():
#     r=Robot()
#     for x in range(10):
#         r.turn(Directions.LEFT)
#         print(r.direction)

# def test_turning_left_right():
#     r=Robot()
#     for x in range(10):
#         r.turn((Directions.LEFT,Directions.RIGHT)[x%2])
#         print(r.direction)

# def testValidate():
#     print(isinstance(5,int))
#     print(utility.validateInteger(5))
#     print(utility.validateString("5"))



# def testDirections():
#     table=Table(5,5)
#     rob=Robot(table,0,0)
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     print("Turning left")
#     rob.turn(Directions.LEFT)
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     print("Turning right")
#     rob.turn(Directions.RIGHT)
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     print("Turning right-right")
#     rob.turn(Directions.RIGHT)
#     rob.turn(Directions.RIGHT)
#     print(f"The direction is {Directions.getDirectinoName(rob.direction)}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     #rob.turn(Directions.LEFT)
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")
#     rob.move()
#     print(f"The x,y pos is {rob.x_pos},{rob.y_pos}")

# @click.command()
# @click.option("--file", default="test/test_data/normal_short_file.dat",prompt="Enter the full path of the file with commands.", help="Name of file with commands.")
# @click.option("--tablex", default="5", prompt="Enter number of squars along x axis",help="Number of squares on table in X direction.")
# @click.option("--tabley", default="5", prompt="Enter number of squars along y axis", help="Number of squares on table in Y direction.")
def makeMovement(file,tablex,tabley):
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
    # print(tablex)
    # print(tabley)




def main():
    if len(sys.argv)!=2:
        print("Invalid arguments length. Usage \n\t start [name of input file]")
        exit()
    else:
        fileName=sys.argv[1]
    makeMovement(fileName,"5","5")

    # r=Robot()
    # test_turning_right()
    # print("-"*30)
    # test_turning_left()
    # print("-"*30)
    # test_turning_left_right()

    #print(utility.validateInteger("5"))

    #testTable()
    #testDirections()
    # print(r.direction)
    #print(f"The direction from {Directions.NORTH}")
    #test_remainder()
    "--------------"
    "--------------"
    #makeMovement("test/test_data/no_place_command.dat","5","5")
