#! /usr/bin/python
#
# Write a compare function that returns 1 ix x>y, 0 if x=y, -1 if x<y
# From http://greenteapress.com/thinkpython/html/thinkpython007.html 

def compare(x, y) :
    if x<y :
        return -1
    elif x==y :
        return 0
    else :
        return 1


print "Testing integers"
assert compare(1, 2) == -1
print "Testing strings"
assert compare("b", "a") == +1
print "Testing tuples"
assert compare((1,2,3),(1,2,3)) == 0
