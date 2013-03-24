#! /usr/bin/python
# Chapter 4 exercises in section 4.3
from TurtleWorld import *
import math



def arc(t, r, num_sides, angle ) :
    """This function uses turtle t and a polygon with number of sides num_sides
to approximate a circle of radius r"""

    circumfrence = math.pi * r
    length = circumfrence / num_sides
    num_sides_to_draw = int ( num_sides * angle / 360.0 )

    for i in range(num_sides_to_draw) :
        fd(t, length)
        lt(t, 360/num_sides)

# This isn't documented in the book yet, but it is required for code re-use.
# If arc.py is executed directly by the python interpreter, then it is the "main"
# module and __name__ will be "__main__" which means that the code below it will
# execute.  However, if this file is imported by another python program, then
# name will be something else, and the code below will not be executed.  This is
# important for exercise 4.1
if __name__ == "__main__" :
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.1 
    arc(bob, 120, 20, 90.0)
    pu(bob)
    fd(bob, 100)      # I just wants the arcs to be separated, this isn't fancy    
    pd(bob)
    arc(bob, 80, 40, 180.0)
    pu(bob)
    fd(bob, 100)      # I just wants the arcs to be separated, this isn't fancy    
    pd(bob)
    arc(bob, 200, 20, 270.0 )
    pu(bob)
    fd(bob, 100)
    pd(bob)
    arc(bob, 200, 20, 360.0 )
    wait_for_user()
