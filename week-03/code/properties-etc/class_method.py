#!/usr/bin/env python

"""
example of a class method
"""

class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def a_class_method(cls, x):
        print "in a_class_method", klass
        return cls( x, x**2 )

#plays well with subclassing:
class C2(C):
    pass
    
if __name__ == "__main__":

    c = C(3, 4)
    print type(c), c.x, c.y
    
    c2 = C.a_class_method(3)
    print type(c2), c2.x, c2.y
    
    c3 = C2.a_class_method(2)
    