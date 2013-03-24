#! /usr/bin/python
#
# From http://greenteapress.com/thinkpython/html/thinkpython007.html
# Chapter 6 exercise 7

#
# This program determines if a given counting number is a power of another
# counting number

def is_power(a, b) :
    assert ( a > 0 )
    assert ( b > 0 )
    if a < b :
        return False
    elif a == b :
        return True
    else :
        if a % b == 0 :
            return is_power ( a/b, b )
        else :
            return False


def test ( a, b ) :
    if is_power ( a, b ) :
        print a, "is a power of", b
    else :
        print a, "is not a power of ", b

test ( 9, 3 )
test ( 3, 3 )
test ( 10, 3 )
test ( 27, 3 )
test ( 3, 9 )
test ( 3, 10 )
test ( 1000, 10 )
test ( 1001, 10 )
test ( 70, 10 )
try :
    test ( 15, 0 )
except AssertionError :
    print "Successfully checked that b cannot be zero"
try :
    test ( 15, -1 )
except AssertionError :
    print "Successfully checked that b cannot be negative"
try :
    test ( -100, 10 )
except AssertionError :
    print "Successfully checked that a cannot be negative"



