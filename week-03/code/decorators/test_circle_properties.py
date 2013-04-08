#!/usr/bin/env python

import pytest

"""
code that tests the circle class defined in circle.py

When run, should result in:

the radius: 4
the diameter: 8
the area: 50.2654824574
the repr(): Circle(4.000000)
the str(): Circle Object with radius: 4.000000

setting the radius to 2:
the radius: 2
the diameter: 4
the area: 12.5663706144

setting the diameter to 6:
the radius: 3.0
the diameter: 6.0
the area: 28.2743338823

trying to delete the diameter
Whoops: can't delete attribute

trying to set the area
Whoops: can't set attribute

adding two circles together
Circle Object with radius: 6.000000

"""

from circle_properties import Circle
#from circle_properties_solution import Circle


def test_basic():
#  "creating a Circle with radius 4"    
    c = Circle(4)
    print "the radius:", c.radius    
    print "the diameter:", c.diameter
    print "the area:", c.area
    print "the repr():", repr(c)
    print "the str():", str(c)
    assert c.radius == 4
    assert c.diameter == 8
    assert round(c.area, 5) == 50.26548

def test_change():
    #  "creating a Circle with radius 4"    
    c = Circle(4)

    #"setting the radius to 2:"
    c.radius = 2
    assert c.radius == 2
    assert c.diameter == 4
    assert round(c.area, 5) == 12.56637

def test_delete():
    # trying to delete the diameter
    c = Circle(4)
    with pytest.raises(AttributeError):
        del c.diameter

def test_set_area():
    # trying to delete the diameter
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 12

def test_add_circles():
    
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2 
    assert c3.radius == 6 
    assert c3.diameter == 12 
