from robot import Robot
import direction
from direction import Directions
import direction
import utility
from table import Table 

def test_remainder():

    for x in range(-10,10):
        print(f"The remainder of {x}%4 is {x%4}")

def test_turning_right():
    r=Robot()
    for x in range(10):
        r.turn(Directions.RIGHT)
        print(r.direction)

def test_turning_left():
    r=Robot()
    for x in range(10):
        r.turn(Directions.LEFT)
        print(r.direction)

def test_turning_left_right():
    r=Robot()
    for x in range(10):
        r.turn((Directions.LEFT,Directions.RIGHT)[x%2])
        print(r.direction)

def testValidate():
    print(isinstance(5,int))
    print(utility.validateInteger(5))
    print(utility.validateString("5"))

def testTable():
    t=Table(5,5)
    print("Table fine")

def main():
    print("In main")
    # r=Robot()
    # test_turning_right()
    # print("-"*30)
    # test_turning_left()
    # print("-"*30)
    # test_turning_left_right()

    #print(utility.validateInteger("5"))

    testTable()

    # print(r.direction)
    #print(f"The direction from {Directions.NORTH}")
    #test_remainder()