#! /usr/bin/python
#
# Draw an Archimedian spiral

import math

from TurtleWorld import *

def draw_spiral(t, n, length, a, b):
    """Draws an Archimedian spiral starting at the origin.  Use Turtle t.  n is
how many line segments to draw.  Length is the length of each line segment.  a
is how loose the initial spiral starts out (larger is looser).  b: how loosly
coiled the spiral is (larger is looser)

http://en.wikipedia.org/wiki/Spiral   """
    
    theta = 0.0         # the angle that the Turtle is at, measured counter clockwise from the X axis

    for i in range(n):
        fd(t, length)
        delta_theta = 1.0 / (a + b * theta)
        lt(t, delta_theta)
        theta += delta_theta

def draw_axis(t) :
    """Draw X and Y axis.  This assumes that the Turtle hasn't moved yet
and is still pointing directly to the right"""
    length = 250
    fd(t,length)
    rt(t,180.0)
    fd(t,length*2)
    rt(t,180.0)
    fd(t,length)
    rt(t,90.0)
    fd(t,length)
    rt(t,180.0)
    fd(t,length*2)
    rt(t,180.0)
    fd(t,length)
    lt(t,90)        # Leave the turtle pointing in the same direction
    
    


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
draw_axis(bob)
draw_spiral(bob, 1000, 5, 0.05, 0.0002 )

wait_for_user()

