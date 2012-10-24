#! /usr/bin/python
#
# Chapter 5 Exercise 4
# The Koch curve is a fractal that looks something like Figure 5.2. To draw a
# Koch curve with length x, all you have to do is
# Draw a Koch curve with length x/3.
# Turn left 60 degrees.
# Draw a Koch curve with length x/3.
# Turn right 120 degrees.
# Draw a Koch curve with length x/3.
# Turn left 60 degrees.
# Draw a Koch curve with length x/3.
# The exception is if x is less than 3: in that case, you can just draw a
# straight line with length x.
# Write a function called koch that takes a turtle and a length as parameters,
# and that uses the turtle to draw a Koch curve with the given length.
# Write a function called snowflake that draws three Koch curves to make the
# outline of a snowflake.

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0          # make the turtle move faster

def koch ( t, length ) :
    """This function draws a koch curve"""
    if length > 3 :
        l_o_3 = length / 3.0
        koch (t, l_o_3 )
        lt(t, 60 )
        koch (t, l_o_3 )
        rt(t, 120)
        koch ( t, l_o_3 )
        lt(t, 60)
        koch ( t, l_o_3 )
    else :
        fd( t, length )

def snowflake ( t, length ) :
    t.set_pen_color('green')
    for i in range(3) :
        koch ( t, length )
        rt (t, 120 )
    
pu(bob)
bk ( bob, 200 )
pd(bob)
koch ( bob, 81 )
snowflake ( bob, 243 )




wait_for_user()
