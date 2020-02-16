import sys
sys.path.append('.')

from table import Table
from rparser import Parser,Command
import pytest

# correct file with indented commands
# to test if all commands are read
def test_correct_file():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    assert p.source==testFileName

    retCommands=[]
    retCommands.append(Command("PLACE 1,2,EAST"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("LEFT"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("REPORT"))

    index=0    
    for cmd in retCommands:
        assert p.allCommands[index]==cmd
        index=index+1

# correct file with indented commands
# to test if start and ene white spacea are ignored
def test_correct_file_indented_commands():
    testFileName="test/test_data/08normal_short_indented.dat"
    p=Parser(testFileName)
    assert p.source==testFileName

    retCommands=[]
    retCommands.append(Command("PLACE 1,2,EAST"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("LEFT"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("REPORT"))

    index=0    
    for cmd in retCommands:
        assert p.allCommands[index]==cmd
        index=index+1

# Should throw error as an invalid statement is used
def test_incorrect_invalid_statement_inbetween():
    testFileName="test/test_data/01invalid_inbetween.dat"
    with pytest.raises(SyntaxError) as excinfo:
        p=Parser(testFileName)


# Should throw error as the file has no PLACE command
def test_incorrect_no_PLACE():
    testFileName="test/test_data/02no_place_command.dat"
    with pytest.raises(SyntaxError) as excinfo:
        p=Parser(testFileName)


# Incorrect non-parsable commands in the first few lines
# after PLACE all commands valid
def test_correct_file_invalid_before_place():
    testFileName="test/test_data/09invalid_in_start.dat"
    p=Parser(testFileName)
    assert p.source==testFileName

    retCommands=[]
    retCommands.append(Command("PLACE 0,0,NORTH"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("LEFT"))
    retCommands.append(Command("RIGHT"))
    retCommands.append(Command("REPORT"))

    index=0    
    for cmd in retCommands:
        assert p.allCommands[index]==cmd
        index=index+1

# testing the method for an all positive scenario
def test_validatePlaceParameters_correct_values():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    valid,message=p.validatePlaceParameters(["0","0","NORTH"])
    assert valid

# testing the method for lesser parameters
def test_validatePlaceParameters_less_than_3_params():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    valid,message=p.validatePlaceParameters(["0","0"])
    assert not valid

# testing the method for non intger X
def test_validatePlaceParameters_non_integer_x():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    valid,message=p.validatePlaceParameters(["A","0","NORTH"])
    assert not valid


# testing the method for non intger Y
def test_validatePlaceParameters_non_integer_y():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    valid,message=p.validatePlaceParameters(["0","G","NORTH"])
    assert not valid

# testing the method for Invalid direction
def test_validatePlaceParameters_incorrect_direction():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    valid,message=p.validatePlaceParameters(["0","0","GGG"])
    assert not valid


# testing the method for non intger X
def test_validatePlaceParameters_negative_integer_x():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    print("The validity to check is")
    valid,message=p.validatePlaceParameters(["-1","0","NORTH"])
    assert not valid


# testing the method for non intger Y
def test_validatePlaceParameters_negative_integer_y():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    valid,message=p.validatePlaceParameters(["3","-1","NORTH"])
    assert not valid


#######################################30

def test_makeCommandArray_correct_values():
    testFileName="test/test_data/03normal_short_file.dat"
    p=Parser(testFileName)
    assert p.source==testFileName

    retCommands=[]
    retCommands.append(Command("PLACE 1,2,EAST"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("LEFT"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("REPORT"))

    p.makeCommandArray()

    index=0    
    for cmd in retCommands:
        assert p.allCommands[index]==cmd
        index=index+1

# correct file with indented commands
# to test if start and ene white spacea are ignored
def test_makeCommandArray_correct_file_indented_commands():
    testFileName="test/test_data/08normal_short_indented.dat"
    p=Parser(testFileName)
    assert p.source==testFileName

    retCommands=[]
    retCommands.append(Command("PLACE 1,2,EAST"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("LEFT"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("REPORT"))

    p.makeCommandArray()

    index=0    
    for cmd in retCommands:
        assert p.allCommands[index]==cmd
        index=index+1

# Incorrect non-parsable commands in the first few lines
# after PLACE all commands valid
def test_makeCommandArray_correct_file_invalid_before_place():
    testFileName="test/test_data/09invalid_in_start.dat"
    p=Parser(testFileName)
    assert p.source==testFileName

    retCommands=[]
    retCommands.append(Command("PLACE 0,0,NORTH"))
    retCommands.append(Command("MOVE"))
    retCommands.append(Command("LEFT"))
    retCommands.append(Command("RIGHT"))
    retCommands.append(Command("REPORT"))

    p.makeCommandArray()

    index=0    
    for cmd in retCommands:
        assert p.allCommands[index]==cmd
        index=index+1

