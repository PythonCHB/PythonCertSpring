# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
"""
some test code to teach me something about how super() works
"""

# <codecell>

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


# <codecell>

print "running traditional way"
c = C()
c.this()



# <codecell>

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


# <codecell>

print "using super in just C"
c = C()
c.this()


# <codecell>

# using super everywhere:


# <codecell>

class Base(object):
    def this(self):
        pass # just so there is a base that has the method


# <codecell>

class A(Base):
    def this(self):
        print "in A.this"
        super(A, self).this()


# <codecell>

class B(Base):
    def this(self):
        print "in B.this"
        super(B, self).this()


# <codecell>

class C(A,B):
    def this(self):
        print "in C.this"
        super(C, self).this()


# <codecell>

print "using super everywhere"
c = C()
c.this()


# <codecell>

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


# <codecell>

print "using super everywhere but C"
c = C()
c.this()


# <codecell>

