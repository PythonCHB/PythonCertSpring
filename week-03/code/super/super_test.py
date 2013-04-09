#!/usr/bin/env python

"""
some example code, demostrating some super() behaviour
"""

class A(object):
    def __init__(self):
        print "in A __init__"
        s = super(A, self).__init__()

class B(object):
    def __init__(self):
        print "in B.__init__"
        s = super(B, self).__init__()

class C(object):
    def __init__(self):
        print "in C.__init__"
        s = super(C, self).__init__()

class D(C, B, A):
    def __init__(self):
       print "in D.__init__"
       super(D, self).__init__()

d = D()

s_c = super(C, d)
print s_c
s_a = super(A, d)
print s_a
s_b = super(B, d)
print s_b

