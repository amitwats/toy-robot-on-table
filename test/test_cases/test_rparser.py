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


# def testConstructor():
#     testFileName="test/test_data/normal_short_file.dat"
#     p=Parser(testFileName)
#     p.isValid()

# def testCommand():
#     # c=Command("PLACE 5,5,NORTH")
#     c=Command("REPORT")
#     # c=Command("")
#     #print(c)
#     print(c.name)
#     print(c.parameters)

# def testParsing():
#     p=Parser(FILE_1)
#     #p=Parser(FILE_3)
#     #p=Parser(FILE_4)
#     p=Parser(FILE_2)
#     print(p.source)
#     x=p.isValid()
#     print(f"The val is {p.isValid()}")
#     print(f"Iteratimg the command array")
#     for cm in p.allCommands:
#         print(cm)



# def test_constructor_all_correct():
#     try:
#         t=Table(5,5)
#         assert True
#     except:
#         assert False

# def test_constructor_x_string_other_correct():
#     with pytest.raises(ValueError) as excinfo:
#         t=Table("5",5)
    
# def test_constructor_y_string_other_correct():
#     with pytest.raises(ValueError) as excinfo:
#         t=Table(5,"5")

# def test_constructor_x_y_string_other_correct():
#     with pytest.raises(ValueError) as excinfo:
#         t=Table("5","5")

# def test_isPositionValid_correct_paramaters():
#     t=Table(5,5)
#     retVal=t.isPositionValid(2,2)
#     expVal=True
#     assert retVal==expVal

# def test_isPositionValid_0_x_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(0,2)
#     expVal=True
#     assert retVal==expVal

# def test_isPositionValid_0_y_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(4,0)
#     expVal=True
#     assert retVal==expVal

# def test_isPositionValid_max_x_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(4,0)
#     expVal=True
#     assert retVal==expVal

# def test_isPositionValid_max_y_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(0,4)
#     expVal=True
#     assert retVal==expVal

# def test_isPositionValid_invalid_y_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(0,5)
#     expVal=False
#     assert retVal==expVal

# def test_isPositionValid_invalid_x_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(5,0)
#     expVal=False
#     assert retVal==expVal

# def test_isPositionValid_neg_y_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(0,-1)
#     expVal=False
#     assert retVal==expVal

# def test_isPositionValid_neg_x_paramater():
#     t=Table(5,5)
#     retVal=t.isPositionValid(-1,0)
#     expVal=False
#     assert retVal==expVal


