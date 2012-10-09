#! /usr/bin/python
#
# Week 8
class A(object) :
    def who_am_i(self) :
        print "Defined in A"
    a = "eh?"

class B(A) :
    def who_am_i(self) :
        print "Defined in B"
    b = "bee"

class C(object) :
    def who_am_i(self) :
        print "Defined in C"
    c = "sea"

class D(C) :
    def who_am_i(self) :
        print "Defined in D"
    d = "Dee" # A river in Wales, see http://en.wikipedia.org/wiki/River_Dee_(Wales)

class E(B,D) :
    def who_am_i(self) :
        print "Defined in E"
    e = "ea."   # an abbreviation for "each"

a = A()
b = B()
c = C()
d = D()
e = E()

if __name__ == "__main__" :

    a.who_am_i()
    b.who_am_i()
    c.who_am_i()
    d.who_am_i()
    e.who_am_i()

    print e.a, e.b, e.c, e.d, e.e
