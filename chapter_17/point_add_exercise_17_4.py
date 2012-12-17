#! /usr/bin/env python
#
#
# Exercise 17-4   Write an add method for the Point class.

class Point( object ):
    """A class which represents a point on a plane"""
    def __init__ ( self, x, y ) :
        """A constructor for a point"""
        self.x = x
        self.y = y

    def __str__ ( self ) :
        """Output a string representation of a Point object"""
        return "["+str(self.x)+","+str(self.y)+"]"

    def __add__ ( self, other ):
        assert isinstance(other, Point),"You didn't add a point to a point"
        r = Point(self.x, self.y )
        r.x += other.x
        r.y += other.y
        return r

if __name__ == "__main__" :
    p = Point(60,240)
    k = p + Point(10,20)
    print k, "Should be 70,260"
    
