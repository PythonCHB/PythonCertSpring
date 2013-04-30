#!/usr/bin/env python

# data types
from start import *

# from scratch:
print np.ones((3,)) # default dtype is float64

print np.zeros((2,3), dtype=np.int32)

print np.empty((3,3), dtype=np.float32) # not initilized!

# for a range:
# integers:
print np.arange(10)
# for floats
print np.linspace(0, 1, 11)

print np.logspace(0, 3, 4)


# from existing data:
 
print np.array([(1, 2),
                (3, 4.0),
                (5, 6)]) # auto-determined dtype

# maybe an array?
a = np.arange(5)
b = np.asarray(a)
print a is b

#or not:
a = range(5)
b = np.asarray(a)
print a is b

print np.ascontiguousarray(a)# forces contiguous datablock

# from binary data:
s = 'abcdefg'
a = np.frombuffer(s, dtype=np.uint8)
print a

print np.fromstring('\x12\x04', dtype=np.uint8) # really should be bytes...

# from (and to) binary file:
a = np.arange(5, dtype=np.float32) # jsut a binary dump!
a.tofile('junk.dat')

print np.fromfile('junk.dat', dtype=np.float32) # need dtype!
