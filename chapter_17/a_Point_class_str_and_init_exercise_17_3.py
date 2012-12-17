#! /usr/bin/env python
#
# Exercise 17-3   Write a str method for the Point class. Create a Point object
# and print it.
#

class Point( object ):
    """A class which represents a point on a plane"""
    def __init__ ( self, x, y ) :
        """A constructor for a point"""
        self.x = x
        self.y = y

    def __str__ ( self ) :
        """Output a string representation of a Point object"""
        return "["+str(self.x)+","+str(self.y)+"]"


p = Point(60,40)
s = str(p)
print s
print p
