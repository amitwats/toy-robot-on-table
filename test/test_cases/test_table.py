import sys
sys.path.append('.')

from table import Table
import pytest

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


