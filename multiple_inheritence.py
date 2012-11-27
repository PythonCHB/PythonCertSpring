#! /usr/bin/python
#
# Week 8
class A(object) :
    def who_am_i(self) :
        print "Defined in A"
    a = "eh?"             # a and c are class attributes
    v = "Parsley"

class B(A) :
    def who_am_i(self) :
        print "Defined in B"
    b = "bee"

class C(object) :
    def who_am_i(self) :
        print "Defined in C"
    c = "sea"
    v = "Rosemary"

class D(C) :
    def who_am_i(self) :
        print "Defined in D"
    d = "Dee" # A river in Wales, see http://en.wikipedia.org/wiki/River_Dee_(Wales)

class E(B,D) :
    def who_am_i(self) :
        print "Defined in E"
    e = "ea."   # an abbreviation for "each"

class F(D,B) :
    def who_ami_i(self) :
        print "Defined in F"
    f = "foolish"    # It's a good thing I am in computers, because if I were
                     # a poet, I would starve

# These 6 statements have to be here because multiple_inheritence.py is imported
# by intro_to_polymorphism.py
a = A()
b = B()
c = C()
d = D()
e = E()
f = F()

if __name__ == "__main__" :
    print "a.v=",a.v
    print "b.v=",b.v
    print "c.v=",c.v
    print "d.v=",d.v
    print "e.v=",e.v
    print "f.v=",f.v

    a.who_am_i()
    b.who_am_i()
    c.who_am_i()
    d.who_am_i()
    e.who_am_i()
    f.who_am_i()

    print "e.a=",e.a,"e.b=", e.b,"e.c=", e.c,"e.d=", e.d,"e.e=", e.e, "f.f=", f.f
    print "a ",("is" if isinstance(a, A) else "is not"), "an instance of A"
    print "a ",("is" if isinstance(a, B) else "is not"), "an instance of B"
    print "b ",("is" if isinstance(b, A) else "is not"), "an instance of A"
    print "b ",("is" if isinstance(b, B) else "is not"), "an instance of B"
    print "e ",("is" if isinstance(e, E) else "is not"), "an instance of E"
    print "e ",("is" if isinstance(e, B) else "is not"), "an instance of B"
    print "e ",("is" if isinstance(e, C) else "is not"), "an instance of C"
    print "f ",("is" if isinstance(f, F) else "is not"), "an instance of F"
    print "f ",("is" if isinstance(f, B) else "is not"), "an instance of B"
    print "f ",("is" if isinstance(f, C) else "is not"), "an instance of C"
    print "f ",("is" if isinstance(f, E) else "is not"), "an instance of E"

