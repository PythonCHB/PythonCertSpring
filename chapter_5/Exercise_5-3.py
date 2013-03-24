#! /usr/bin/python
#
#
# Read the following function and see if you can figure out what it does. Then
# run it (see the examples in Chapter 4).

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

length = float ( raw_input ("Enter a starting length ") )
n = int ( raw_input ( "Enter the number of levels of recursion " ) )
pu(bob)
bk(bob, length*n )
pd(bob)
draw ( bob, length, n )


wait_for_user()
