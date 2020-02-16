import sys
sys.path.append('.')

from rparser import Parser,Command
import pytest

# 2 params with command valid case
def test_valid_constructor_command_2_parameters():
    c=Command("CMD par1,par2")
    assert c.name=="CMD"
    assert c.parameters[0]=="par1"
    assert c.parameters[1]=="par2"

# 0 params with command valid case
def test_valid_constructor_command_0_parameters():
    c=Command("CMD")
    assert c.name=="CMD"
    assert len(c.parameters)==0

# 0 params with command with space valid case
def test_valid_constructor_command_with_space_0_parameters():
    c=Command("CMD ")
    assert c.name=="CMD"
    assert len(c.parameters)==0

# 0 params with command with space before comand valid case
def test_valid_constructor_command_with_space_before_0_parameters():
    c=Command(" CMD ")
    assert c.name=="CMD"
    assert len(c.parameters)==0

# 2 params with command with space before comand valid case
def test_valid_constructor_command_with_space_before_2_parameters():
    c=Command(" CMD    par1,par2")
    assert c.name=="CMD"
    assert c.parameters[0]=="par1"
    assert c.parameters[1]=="par2"

# 2 params with command with space before comand valid case
def test_valid_constructor_command_with_space_after_2_parameters():
    c=Command(" CMD    par1,par2   ")
    assert c.name=="CMD"
    assert c.parameters[0]=="par1"
    assert c.parameters[1]=="par2"


# 0 params with no command
def test_valid_constructor_no_command_no_parameters():
    c=Command("")
    assert c.name==""
    assert len(c.parameters)==0

# 0 params with no command
def test_valid_constructor_no_command_no_parameters_spaces():
    c=Command("     ")
    assert c.name==""
    assert len(c.parameters)==0

# 2 param secnd blank with command with space before comand valid case
def test_valid_constructor_command_with_space_after_2_parameters_one_blank():
    c=Command(" CMD    par1,")
    assert c.name=="CMD"
    assert c.parameters[0]=="par1"
    assert c.parameters[1]==""

# 3 param secnd blank with command with space before comand valid case
def test_valid_constructor_command_with_space_after_3_parameters_one_blank():
    c=Command(" CMD    par1,,par3")
    assert c.name=="CMD"
    assert c.parameters[0]=="par1"
    assert c.parameters[1]==""
    assert c.parameters[2]=="par3"

def test_equality_cmd_3_valid_params():
    c1=Command(" CMD par1,par2,par3")
    c2=Command(" CMD par1,par2,par3")
    assert c1==c2

def test_equality_cmd_3_valid_params_white_spaces():
    c1=Command(" CMD par1,par2,par3")
    c2=Command(" CMD   par1, par2,par3")
    assert c1==c2


def test_equality_cmd_0_valid_params():
    c1=Command("CMD")
    c2=Command("CMD")
    assert c1==c2

def test_equality_cmd_0_valid_params_white_spaces():
    c1=Command(" CMD   ")
    c2=Command(" CMD")
    assert c1==c2


def test_equality_cmd_1_valid_params():
    c1=Command(" CMD  par1")
    c2=Command(" CMD par1")
    assert c1==c2


def test_to_str_cmd_1_valid_params():
    c=Command(" CMD  par1")
    assert str(c)=="name=CMD and parameters are ['par1']"


