#! /usr/bin/python
#
#
class A(object) :
    x = 1.0
    z = "spam!"

class B(A) :
    y = 2.7
    z = "vikings"

b = B( )

print b.x, b.y, b.z

a = A( )
print a.x, a.z

