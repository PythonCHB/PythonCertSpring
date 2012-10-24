#! /usr/bin/python
# -*- coding: utf-8 -*-
# The Ackermann function, A(m, n), is defined:
# A(m, n) = 	
#               n+1	if  m = 0 
#         A(m−1, 1)	if  m > 0  and  n = 0 
# A(m−1, A(m, n−1))	if  m > 0  and  n > 0.
# 
# See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named 
# ack that evaluates Ackerman’s function. Use your function to evaluate 
# ack(3, 4), which should be 125. What happens for larger values of m and n? 


def ack ( m, n ) :
    """An implementation of the Ackermann function"""
    assert m >= 0
    assert n >= 0
    if m == 0 :
        return n + 1
    else :             # m > 0, since if m is < 0, then the assert will fail
        if n == 0 :
            return ack ( m-1, 1 )
        else :        # n > 0, since if n is < 0, then the assert will fail
            return ( ack ( m-1, ack(m, n-1) ) )

print "Testing that the ack(3,4) is 125 ",
assert ack(3,4) == 125
print "Test passed"
while True :
    m = int ( raw_input ( "Enter m >> " ) )
    n = int ( raw_input ( "Enter n >> " ) )
    print "ack(",m,",",n,") is ", ack(m,n)


