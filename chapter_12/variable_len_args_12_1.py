#! /usr/bin/env python
#
#
# Exercise 1   Many of the built-in functions use variable-length argument tuples.
# For example, max and min can take any number of arguments:
# >>> max(1,2,3)
# 3
# But sum does not.
#
# >>> sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3
#
# Write a function called sumall that takes any number of arguments and returns
# their sum.


def sumall ( *t ):
    """This function calculates the sum of all of its arguments"""
    s = 0
    for i in range(len(t)) :
        s += t[i]
    return s

if __name__ == "__main__" :
    def test_sumall(expected, *u ) :
        r = sumall( *u )
        if r == expected :
            print "Success: sumall returned",r," as expected.  Args are %s" % \
                  str(u)
        else:
            print "FAILURE: sumall returned",r," but expected ",expected,".  Args are %s" % \
                   str(u)

    test_sumall ( 10, 1, 3, 6 )
    test_sumall ( 20.0, 1.0, 10, 2, 2, 5 )
    test_sumall ( (1+2j), 1, (1+1j), (-1+1j) )    
    
            
    
