# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# data types
from start import *


# <codecell>

# from scratch:
print np.ones((3,)) # default dtype is float64


# <codecell>

print np.zeros((2,3), dtype=np.int32)


# <codecell>

print np.empty((3,3), dtype=np.float32) # not initilized!


# <codecell>

# for a range:
# integers:
print np.arange(10)


# <codecell>

# for floats
print np.linspace(0, 1, 11)


# <codecell>

print np.logspace(0, 3, 4)



# <codecell>

# from existing data:
 
print np.array([(1, 2),
                (3, 4.0),
                (5, 6)]) # auto-determined dtype


# <codecell>

# maybe an array?
a = np.arange(5)
b = np.asarray(a)
print a is b


# <codecell>

#or not:
a = range(5)
b = np.asarray(a)
print a is b


# <codecell>

print np.ascontiguousarray(a)# forces contiguous datablock


# <codecell>

# from binary data:
s = 'abcdefg'
a = np.frombuffer(s, dtype=np.uint8)
print a


# <codecell>

print np.fromstring('\x12\x04', dtype=np.uint8) # really should be bytes...


# <codecell>

# from (and to) binary file:
a = np.arange(5, dtype=np.float32) # jsut a binary dump!
a.tofile('junk.dat')


# <codecell>

print np.fromfile('junk.dat', dtype=np.float32) # need dtype!

# <codecell>

