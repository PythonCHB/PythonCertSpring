#! /usr/bin/env python
#
# Do not make this common error

def wrong(w):
    return lambda x: x+n

print wrong(2.3)
e = wrong(11.2)

try:
    q = e(0.75)
except NameError,m:
    print "Well, I guess there was a name error \n%s" % m

n = 14
q2 = e(0.85)
print q2

