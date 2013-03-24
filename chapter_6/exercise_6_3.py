#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#
# http://greenteapress.com/thinkpython/html/thinkpython007.html
# Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.

def is_between ( x, y, z ) :
    return ( x<=y<=z )

def test ( x, y, z, expected ) :
    """This function documents the testing process.  x, y, z are arguments to
the function under test, is_between.  exprected is the expected result, either
True or False"""
    print "Testing ", x, y, z
    assert ( is_between ( x, y, z ) == expected )

    
test( 1, 2, 3, True )
test( 1, 2, 2, True )
test( 1, 1, 3, True )
test( 1, 1, 1, True )
test( 1, 3, 2, False )
test( 3, 1, 2, False )
test( 1, 2, 1, False )

