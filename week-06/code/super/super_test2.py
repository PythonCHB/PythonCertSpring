#!/usr/bin/env python

"""
some test code to teach me something about how super() works
"""

# the "old way":

class A(object):
    def this(self):
        print "in A.this"

class B(object):
    def this(self):
        print "in B.this"

class C(A,B):
    def this(self):
        print "in C.this"
        A.this(self)
        B.this(self)

print "running traditional way"
c = C()
c.this()

# using super in just C:


class A(object):
    def this(self):
        print "in A.this"

class B(object):
    def this(self):
        print "in B.this"

class C(A,B):
    def this(self):
        print "in C.this"
        super(C, self).this()

print 
print "using super in just C"
c = C()
c.this()

# using super everywhere:

class Base(object):
    def this(self):
        pass # just so there is a base that has the method

class A(Base):
    def this(self):
        print "in A.this"
        super(A, self).this()

class B(Base):
    def this(self):
        print "in B.this"
        super(B, self).this()

class C(A,B):
    def this(self):
        print "in C.this"
        super(C, self).this()

print 
print "using super everywhere"
c = C()
c.this()

# using super everywhere:

class Base(object):
    def this(self):
        pass # just so there is a base that has the method

class A(Base):
    def this(self):
        print "in A.this"
        s = super(A, self)
        print s
        print s.this
        s.this()

class B(Base):
    def this(self):
        print "in B.this"
        s = super(B, self)
        print s
        print s.this
        s.this()

class C(A,B):
    def this(self):
        print "in C.this"
        A.this(self)
        B.this(self)

print 
print "using super everywhere but C"
c = C()
c.this()

