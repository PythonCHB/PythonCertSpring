#!/usr/bin/env python

# basic array methods:
from start import *

# reshaping:

a = np.arange(12)

print a.shape
a.shape = (3,4)
print a

print np.reshape(a, (2,6) )

# unknown dimension
a.shape = ( -1, 2)
print a

# flatten
for i in a.flat: # iterator
    print i # iterator

print np.ravel(a)

print a.T

print 

# checking dimensions:
a = np.ravel(a)

print np.atleast_2d(a)

# reducing:
a.shape = (2,1,6)
b = np.squeeze(a)
print b.shape

# re-arranging:
print b
print np.flipud(b)
print np.fliplr(b)

