#! /usr/bin/env python
#
# Demonstrates the differences between instance attributes
# and  class attributes


class A(object) :
    c = None          # c is a class variable
    def __init__ ( self,x ) :
        self.i = x
a1 = A(3)
a2 = A(4)
A.c = 16
print a1 is a2
print a1.c, a2.c
print a1.c is a2.c
print a1.i, a2.i

