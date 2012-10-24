#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# From http://greenteapress.com/thinkpython/html/thinkpython007.html
# Chapter 6 exercise 8
# Euclid's algorithm to find the greatest common divisor
# One way to find the GCD of two numbers is Euclid’s algorithm, which is based
# on the observation that if r is the remainder when a is divided by b, then
# gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.


def gcd ( a, b ) :
    if b == 0 :
        return a
    else :
        r = a % b
        return gcd( b, r )


def test ( a, b, g ) :
    """This function verifies that the GCD of a and b is g """
    gt = gcd ( a, b )
    if gt == g :
        print "The GCD of ",a, b, "is, in fact, ", g
    else :
        print "PROBLEM: the GCD of ",a,b, "should be ",g, "but ",gt, "was returned"


test ( 12, 3, 3 )
test ( 8, 9, 1 )
test ( 20, 30, 10 )
test ( 14, 21, 7 )
test ( 21, 14, 7 )
test ( 28, 14, 14 )

        

