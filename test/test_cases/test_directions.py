import sys
sys.path.append('.')

import pytest
from direction import Directions

def test_validate_all_directions_present():
    assert Directions.NORTH==0
    assert Directions.EAST==1
    assert Directions.SOUTH==2
    assert Directions.WEST==3
    assert Directions.RIGHT==1
    assert Directions.LEFT==-1

def test_validTurns():
    retVal=Directions.validTurns()
    expVal=[Directions.RIGHT,Directions.LEFT]
    if len(retVal)==len(expVal):
        for index in range(len(retVal)):
            assert retVal[index]==expVal[index]

def test_validDirections():
    retVal=Directions.validDirections()
    expVal=[Directions.NORTH,Directions.EAST,Directions.SOUTH,Directions.WEST]
    if len(retVal)==len(expVal):
        for index in range(len(retVal)):
            assert retVal[index]==expVal[index]

def test_validDirectionNames():
    retVal=Directions.validDirectionNames()
    expVal=['NORTH','EAST','SOUTH','WEST']
    if len(retVal)==len(expVal):
        for index in range(len(retVal)):
            assert retVal[index]==expVal[index]

def test_validTurnNames():
    retVal=Directions.validTurnNames()
    expVal=['LEFT','RIGHT']
    if len(retVal)==len(expVal):
        for index in range(len(retVal)):
            assert retVal[index]==expVal[index]


def test_getDirectinoName():
    assert Directions.getDirectinoName(0)=="NORTH"
    assert Directions.getDirectinoName(1)=="EAST"
    assert Directions.getDirectinoName(2)=="SOUTH"
    assert Directions.getDirectinoName(3)=="WEST"


def test_getDirectinoName_out_of_range_value():
    assert Directions.getDirectinoName(-1)=="WEST"
    assert Directions.getDirectinoName(4)=="NORTH"

def test_getDirectinoName_invalid_value():
    with pytest.raises(ValueError) as excinfo:
        d=Directions.getDirectinoName("AA")

def test_getDirectinoName():
    assert Directions.getDirectinoName(0)=="NORTH"
    assert Directions.getDirectinoName(1)=="EAST"
    assert Directions.getDirectinoName(2)=="SOUTH"
    assert Directions.getDirectinoName(3)=="WEST"


def test_getDirectionValue_out_of_range_value():
    assert Directions.getDirectionValue("NORTH")==0
    assert Directions.getDirectionValue("EAST")==1
    assert Directions.getDirectionValue("SOUTH")==2
    assert Directions.getDirectionValue("WEST")==3

def test_getDirectionValue_invalid_value():
    with pytest.raises(ValueError) as excinfo:
        d=Directions.getDirectinoName("AA")

