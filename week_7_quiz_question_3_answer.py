#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# THe answer to the third question of the week 7 quiz: Create a class that has
# a __str__ function.  Test it by making an instance of the class and then use
# the print statement to print the instance.


class C(object):
    def __init__(self, a, b=3):
        self.a = a
        self.b = b
        self.c = 16

    def __str__( self ) :
        return "a is "+str(self.a)+" b is "+str(self.b)+" c is "+str(self.c)

j = C(2.5, "Baked beans")
k = C((2+3.4j))
print "j is {",j,"}"
print "k is {",k,"}"
print repr(j)
print repr(k)

