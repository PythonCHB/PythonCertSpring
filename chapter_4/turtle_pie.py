#! /usr/bin/python
#
# Write an appropriately general set of functions that can draw shapes as in Figure 4.2.
#
# Each pie slice is an isoceles triangle with a central angle of 360/N
# The other interior angles are (180 - central_angle) / 2 (The sum of the
# interior angles of a triangle always sum to 180.0. CA+OA+OA=180.0 => CA+2OA=180.0
# => OA = 90.0 - CA/2.  Note that N>=2
#
import math

from TurtleWorld import *


def isoceles_triangle (t, central_angle, radius ) :
    """Using the current orientation of the turtle t as a starting direction,
draw an isoceles triangle with central angle central_angle.  The length of the
equal sides will be radius.  The length of the outer side will be calculated
using trigonometry.
"""
    # The cosine law for general triangles.  C = SQRT(A**2 + B**2 - 2*A*B*cos(theta) )
    # See http://en.wikipedia.org/wiki/Law_of_cosines

    fd(t, radius)
    other_angle = 90.0 - central_angle/2.0
    lt(t, 180.0 - other_angle)
    fs = math.sqrt( 2*radius**2 - 2 * radius**2 * math.cos( math.radians ( central_angle ) ) )
    fd(t, fs)
    lt(t, 180.0 - other_angle)
    fd(t, radius)
    lt(t, 180.0 - central_angle)   # The turtle winds up pointing in the same direction
                            # it did when it started.

def draw_pie ( t, N, r ) :
    """Draw a pie chart with N triangles and radius r using turtle t"""
    central_angle = 360.0 / N
    for i in range(N) :
        isoceles_triangle ( t, central_angle, r )
        lt(t, central_angle )

def move(t, length):
    """Move Turtle t forward length without leaving a trail.  Leaves the pen
down.  This assumes that the turtle is facing right"""
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01        # speed up the turtles
move ( bob, -100 )
draw_pie( bob, 5, 80 )
move( bob, 100 )
draw_pie ( bob, 8, 80 )
move( bob, 100 )
draw_pie ( bob, 6, 80 )

wait_for_user()
                        
