import sys
sys.path.append('.')

from table import Table
from rparser import Parser,Command
import pytest


def testFile():
    testFileName="test/test_data/normal_short_file.dat"

    with open(testFileName) as f:
        lines=[line.rstrip() for line in f]
    for line in lines:
        print(Parser.getCommandType(line))

def testConstructor():
    testFileName="test/test_data/normal_short_file.dat"
    p=Parser(testFileName)
    p.isValid()

def testCommand():
    # c=Command("PLACE 5,5,NORTH")
    c=Command("REPORT")
    # c=Command("")
    #print(c)
    print(c.name)
    print(c.parameters)

def testParsing():
    p=Parser(FILE_1)
    #p=Parser(FILE_3)
    #p=Parser(FILE_4)
    p=Parser(FILE_2)
    print(p.source)
    x=p.isValid()
    print(f"The val is {p.isValid()}")
    print(f"Iteratimg the command array")
    for cm in p.allCommands:
        print(cm)



def test_constructor_all_correct():
    try:
        t=Table(5,5)
        assert True
    except:
        assert False

def test_constructor_x_string_other_correct():
    with pytest.raises(ValueError) as excinfo:
        t=Table("5",5)
    
def test_constructor_y_string_other_correct():
    with pytest.raises(ValueError) as excinfo:
        t=Table(5,"5")

def test_constructor_x_y_string_other_correct():
    with pytest.raises(ValueError) as excinfo:
        t=Table("5","5")

def test_isPositionValid_correct_paramaters():
    t=Table(5,5)
    retVal=t.isPositionValid(2,2)
    expVal=True
    assert retVal==expVal

def test_isPositionValid_0_x_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(0,2)
    expVal=True
    assert retVal==expVal

def test_isPositionValid_0_y_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(4,0)
    expVal=True
    assert retVal==expVal

def test_isPositionValid_max_x_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(4,0)
    expVal=True
    assert retVal==expVal

def test_isPositionValid_max_y_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(0,4)
    expVal=True
    assert retVal==expVal

def test_isPositionValid_invalid_y_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(0,5)
    expVal=False
    assert retVal==expVal

def test_isPositionValid_invalid_x_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(5,0)
    expVal=False
    assert retVal==expVal

def test_isPositionValid_neg_y_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(0,-1)
    expVal=False
    assert retVal==expVal

def test_isPositionValid_neg_x_paramater():
    t=Table(5,5)
    retVal=t.isPositionValid(-1,0)
    expVal=False
    assert retVal==expVal


