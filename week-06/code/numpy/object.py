#!/usr/bin/env python

# Object arrays:
from start import *

# create an empty array:

a = np.empty((2,3), dtype=np.object)

print a

# put stuff into it:

a[0,0] = "a string"
a[0,1] = 4.5
a[0,2] = (1,2,3)
a[1,:] = [6, {'a':3}, 3.4]

print a

# a row:
print a[1,:]

# a column:
print a[:,1]

# an item (a dict in this case)
print a[1,1]
print a[1,1]['a']

