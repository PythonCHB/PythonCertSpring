#! /usr/bin/env python
#
# Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding dx
# to the x coordinate of corner and adding dy to the y coordinate of corner.

class Point ( object ) :
    """represents a point in 2-D space"""
    pass


class Rectangle(object):
    """represent a rectangle.  Attributes: width, height, corner."""
    pass

def move_rectangle( r, dx, dy ):
    r.corner.x += dx
    r.corner.y += dy

def print_rectangle ( r ) :
    assert isinstance (r, Rectangle)
    print "Corner ",r.corner.x, r.corner.y, "and corner ", r.corner.x+r.width, \
          r.corner.y + r.height

if __name__ == "__main__" :
    box = Rectangle()
    box.width = 4.0
    box.height = 2.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print_rectangle ( box )
    move_rectangle ( r=box, dx=3, dy=7 )
    print_rectangle ( box )

    
