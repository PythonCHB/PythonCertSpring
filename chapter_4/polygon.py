#! /usr/bin/python
# Chapter 4 exercises in section 4.3
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def polygon(t, length, num_sides) :
    """This function uses turtle t to draw a polygon with number of sides num_sides"""
    for i in range(num_sides) :
        fd(t, length)
        lt(t, 360/num_sides)


polygon(bob, 100, 5)
polygon(bob, 60, 8)
polygon(bob, 40, 12)

wait_for_user()
