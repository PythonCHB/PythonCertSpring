#! /usr/bin/env python
#
# snafu.py
# This program is hopelessly screwed up - it is an exercise in using the
# debugger
#
#
import math
import pdb; pdb.set_trace()   # for ipython

def discriminant(A, B, C) :
    assert A != 0.0
# Really should be 4 instead of 2, in case you forgot    
    r = math.sqrt(B*B - 2*A*C)
    return r


#  This is a useless comment
A = float(raw_input("Enter A "))
B = float(raw_input("Enter B "))
C = float(raw_input("Enter C "))

try :
    d = discriminant(C, B, A)
except AssertionError, e:
    pdb.set_trace()
except ValueError, e:
    pdb.set_trace()
    

r1 = (-B + d)/(2*A)
r2 = (-B - d)/(2*A)
print "The roots are %f and %f" % ( r1, r2)

          

