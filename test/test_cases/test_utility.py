import sys
sys.path.append('.')

import pytest
import utility


def test_validateType():
    assert utility.validateType(5,int)==5
    assert utility.validateType("5",str)=="5"
    with pytest.raises(ValueError) as excinfo:
        utility.validateType("5",int)

def test_validateInteger():
    assert utility.validateType(5,int)==5
    with pytest.raises(ValueError) as excinfo:
        utility.validateType("A",int)

def test_validateString():
    assert utility.validateType("ABC",str)=="ABC"
    with pytest.raises(ValueError) as excinfo:
        utility.validateType(5,str)


