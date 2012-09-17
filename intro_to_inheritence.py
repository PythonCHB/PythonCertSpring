#! /usr/bin/python
#
#

class A(object) :
    def who_am_i(self):
        print "I am in class A"
    favorite_color = "Blue"
    y = "Why?"

class B(A) :
    def who_am_i(self):
        print "I am in class B"
    favorite_color = "Green"
    x = 42

a = A()
a.who_am_i()
try :
    print a.x
except AttributeError, e :
    print "WHOOPS!", e
print a.y

b = B()
b.who_am_i()
print b.x
print b.y


        
