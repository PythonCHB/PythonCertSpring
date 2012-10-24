#! /usr/bin/python
# This program draws a flower.  A flower is composed of N petals.  Each petal is
# 2 arcs, flipping 180 degrees

from TurtleWorld import *



import pdb

def arc(t, r, num_sides, angle ) :
    """This function uses turtle t and a polygon with number of sides num_sides
to approximate a circle of radius r"""
    import math
    circumfrence = math.pi * r
    length = circumfrence / num_sides
    num_sides_to_draw = round ( num_sides * angle / 360.0 )

    turn = 360.0/num_sides
    lt(t, turn/2.0)
    for i in range(num_sides_to_draw) :
        fd(t, length)
        lt(t, turn)
    rt(t, turn/2.0)


def petal(t, r, num_sides, angle):
    """Draws a petal using two arcs.  t is a Turtle, r: radius of the arcs, and
angle (degrees) that subtends the arcs"""
    for i in range(2):
        arc(t, r, num_sides, angle)        # From the exercise in section 4.3.  Assume
        lt(t, 180-angle)
        

def flower(t, r, n, angle):
    """Draws a flower with n petals. t is a Turtle, n is the number of petals
r is radius of the arcs that create the petals, and angle (degrees) is what
subtends the arcs"""
    for i in range(n):
        petal(t, r, 40, angle)      # 40 is the number of segments in the arc.
        lt(t, (360.0/n) )


def move(t, length):
    """Move Turtle t forward length without leaving a trail.  Leaves the pen
down.  This assumes that the turtle is facing right"""
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1        # speed up the turtles

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
if 1==1 :
    angle = 85.0
    r = 200
    n = 8
    pdb.set_trace()
    arc(bob, 100, 8, 360.0 )    # draw a circle
    move(bob, 100)
    flower(bob, r, n, angle )

       
else:
    flower(bob, 80, 6, 60.0)
    move(bob, 100)
    flower(bob, 80, 8, 45.0)
    move(bob, 100)
    flower(bob, 80, 8, 90.0)

#move(bob, 100)
#flower(bob, 20, 140, 20.0)


wait_for_user()
