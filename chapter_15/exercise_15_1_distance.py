#! /usr/bin/env python
#
# Exercise 15-1   Write a function called distance that takes two Points as
# arguments and returns the distance between them.
import math

class Point ( object ) :
    """represents a point in 2-D space"""
    pass
    
def distance (p_1, p_2 ) :
    """The distance between point p_1 and p_2 """
    h = ( p_1.x - p_2.x ) ** 2 + (p_1.y - p_2.y)**2
    return math.sqrt(h)

if __name__ == "__main__" :
    def test_distance ( p1, p2, answer ) :
        """This tests distance"""
        d = distance ( p1, p2 )
        if abs( d - answer ) < 1.0E-14 :
            print "Passed"
        else :
            print "FAILED: p1=", p1.x, p1.y, "p2=", p2.x, p2.y

    p1 = Point()
    p2 = Point()
    p1.x = 1
    p1.y = 2
    p2.x = 4
    p2.y = -2
    test_distance (p1, p2, 5 )
    dx = 3.4
    dy = 2.7
    p2.x, p2.y = ( p1.x + dx, p1.y + dy )
    test_distance (p1, p2, math.hypot( dx, dy ) )
    

    
