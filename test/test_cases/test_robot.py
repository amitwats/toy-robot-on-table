import sys
sys.path.append('.')

import pytest
from robot import Robot
from direction import Directions
from table import Table

def test_constructor_valid_values():
    t=Table(5,5)
    r=Robot(t,init_x=1,init_y=2,direction=Directions.NORTH)

def test_constructor_string_x():
    t=Table(5,5)
    with pytest.raises(ValueError) as excinfo:
        r=Robot(t,init_x="1",init_y=2,direction=Directions.NORTH)

def test_constructor_string_y():
    t=Table(5,5)
    with pytest.raises(ValueError) as excinfo:
        r=Robot(t,init_x=1,init_y="2",direction=Directions.NORTH)

def test_constructor_invalid_direction():
    t=Table(5,5)
    with pytest.raises(ValueError) as excinfo:
        r=Robot(t,init_x=1,init_y=2,direction="NORTH")


def test_turn_left():
    t=Table(5,5)
    r=Robot(t,init_x=1,init_y=2,direction=Directions.NORTH)
    r.turn(Directions.LEFT)
    assert r.direction==Directions.WEST
    r.turn(Directions.LEFT)
    assert r.direction==Directions.SOUTH
    r.turn(Directions.LEFT)
    assert r.direction==Directions.EAST
    r.turn(Directions.LEFT)
    assert r.direction==Directions.NORTH


def test_turn_right():
    t=Table(5,5)
    r=Robot(t,init_x=1,init_y=2,direction=Directions.NORTH)
    r.turn(Directions.RIGHT)
    assert r.direction==Directions.EAST
    r.turn(Directions.RIGHT)
    assert r.direction==Directions.SOUTH
    r.turn(Directions.RIGHT)
    assert r.direction==Directions.WEST
    r.turn(Directions.RIGHT)
    assert r.direction==Directions.NORTH



def test_move_one_step_ahead():
    t=Table(5,5)
    r=Robot(t,init_x=1,init_y=2,direction=Directions.NORTH)
    r.move()
    assert r.x_pos==1 and r.y_pos==3

    r=Robot(t,init_x=1,init_y=2,direction=Directions.SOUTH)
    r.move()
    assert r.x_pos==1 and r.y_pos==1

    r=Robot(t,init_x=1,init_y=2,direction=Directions.WEST)
    r.move()
    assert r.x_pos==0 and r.y_pos==2

    r=Robot(t,init_x=1,init_y=2,direction=Directions.EAST)
    r.move()
    assert r.x_pos==2 and r.y_pos==2



def test_move_one_step_ahead_borderline():
    t=Table(5,5)
    r=Robot(t,init_x=4,init_y=4,direction=Directions.NORTH)
    r.move()
    assert r.x_pos==4 and r.y_pos==4

    r=Robot(t,init_x=4,init_y=4,direction=Directions.EAST)
    r.move()
    assert r.x_pos==4 and r.y_pos==4

    r=Robot(t,init_x=4,init_y=0,direction=Directions.SOUTH)
    r.move()
    assert r.x_pos==4 and r.y_pos==0

    r=Robot(t,init_x=0,init_y=0,direction=Directions.WEST)
    r.move()
    assert r.x_pos==0 and r.y_pos==0

