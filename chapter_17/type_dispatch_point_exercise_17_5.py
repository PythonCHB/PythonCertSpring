#! /usr/bin/env python
#
#
# Exercise 17-5  Write an add method for Points that works with either a Point
# object or a tuple: If the second operand is a Point, the method should return
# a new Point whose x coordinate is the sum of the x coordinates of the operands,
# and likewise for the y coordinates.
# If the second operand is a tuple, the method should add the first element of
# the tuple to the x coordinate and the second element to the y coordinate, and
# return a new Point with the result.

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
        r = Point(self.x, self.y )
        if type(other) == type((1,3)) :
            r.x += other[0]
            r.y += other[1]
        elif isinstance(other, Point) :
            r.x += other.x
            r.y += other.y
        else :
            raise ValueError,"The second argument was neither a Point or a tuple"
        return r

if __name__ == "__main__" :
    p = Point(60,240)
    k = p + Point(10,20)
    print k, "Should be 70,260"
    w = p + (-10,-30)
    print w, "Should be 50,210"

    
