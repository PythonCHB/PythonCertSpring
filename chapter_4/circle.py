#! /usr/bin/python
# Chapter 4 exercises in section 4.3
from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

def polygon(t, length, num_sides) :
    """This function uses turtle t to draw a polygon with number of sides num_sides"""
    for i in range(num_sides) :
        fd(t, length)
        lt(t, 360/num_sides)

def circle(t, r, num_sides ) :
    """This function uses turtle t and a polygon with number of sides num_sides
to approximate a circle of radius r"""

    circumfrence = math.pi * r
    length = circumfrence / num_sides

    polygon(t, length, num_sides)

    
circle(bob, 120, 20)
circle(bob, 80, 40)

wait_for_user()
