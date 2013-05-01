# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>



import numpy as np

#from start import *

# assorted data types:


# <codecell>

# usually defaults to float(64 bit)
a = np.ones(3)
print a.dtype


# <codecell>

# smart enough to match input:
a = np.array((3,5,7,8))
print a.dtype


# <codecell>

# smart enough to match input:
a = np.array((3.0,5,7,8))
print a.dtype


# <codecell>

# or you can specify:
a = np.array( (1,2,3), dtype=np.uint8 )
print a.dtype


# <codecell>

#careful: integers overflow:
a = np.array( (1, 10, 100,), dtype=np.uint8)

print a

a *= 3

print a



# <codecell>

# Object arrays:

# create an empty array:

a = np.empty((2,3), dtype=np.object)

print a


# <codecell>

# put stuff into it:

a[0,0] = "a string"
a[0,1] = 4.5
a[0,2] = (1,2,3)
a[1,:] = [6, {'a':3}, 3.4]

print a


# <codecell>

# a row:
print a[1,:]


# <codecell>

# a column:
print a[:,1]


# <codecell>

# an item (a dict in this case)
print a[1,1]

# <codecell>

print a[1,1]['a']


# <codecell>

