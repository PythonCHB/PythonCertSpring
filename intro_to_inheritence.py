#! /usr/bin/python
#
#

class A(object) :
    c = "Sea"
    def who_am_i(self):
        print "I am in class A"
    favorite_color = "Blue"
    y = "Why?"

class B(A) :
    c = "Ocean"
    def who_am_i(self):
        print "I am in class B"
    favorite_color = "Green"
    x = 42

a = A()
a.who_am_i()
print a.c
try :
    print a.x
except AttributeError, e :
    print "WHOOPS!", e
print a.y

b = B()
b.who_am_i()
print b.c
print b.x
print b.y

print "a ",("is" if isinstance(a, A) else "is not"), "an instance of A"
print "a ",("is" if isinstance(a, B) else "is not"), "an instance of B"
print "b ",("is" if isinstance(b, A) else "is not"), "an instance of A"
print "b ",("is" if isinstance(b, B) else "is not"), "an instance of B"


        
