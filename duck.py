#! /usr/bin/env python
#
#
# This program demonstrates "duck typing", which is a form of polymorphism
# Week 8
#
class A(object) :
    pass

class C(object) :
    pass

class B(A):
    def f(self, x):
        print "I am in function f in class B, x is ", x

class D(C):
    def f(self, x):
        print "I am in function f in class D, x is ", x


b = B()
d = D()

b.f("instance b")
d.f("instance d")

def do_something(z):
    print "In do_something",
    y = 42   # A different universe of humor
    z.f(y)
   

print "calling do_something with b", 
do_something(b)
print "calling do_something with d", 
do_something(d)

