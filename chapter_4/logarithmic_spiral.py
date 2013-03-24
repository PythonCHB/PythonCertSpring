#! /usr/bin/python
#
# Draw an Archimedian spiral

import math

from TurtleWorld import *

def draw_spiral(t, n, length, angle ):
    """Draws a logarithmic spiral starting at the origin.  Use Turtle t.  n is
how many line segments to draw.  Length is the length of each line segment.  angle
is the angle between a tangent to the spiral and the tangent to the spiral at
the next point

http://en.wikipedia.org/wiki/Spiral and http://en.wikipedia.org/wiki/Logarithmic_spiral   """
        

    for i in range(n):
        fd(t, length)
        lt(t, angle )


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
draw_spiral(bob, 1000, 5, 15.17 )

wait_for_user()

