#!/usr/bin/env python

"""
examples of a static method
"""

class C(object):

    @staticmethod
    def add(a, b):
        print "in a_static_method"
        return a+b
    
if __name__ == "__main__":

    # called from the class object
    print C.add(3,4)
    
    # called  from a class instance
    c = C()
    print c.add(4,5)
    
    