#!/usr/bin/env python

from start import *

print "size of empty list:"
print sys.getsizeof([])

print "size of empty ndarray:"
print sys.getsizeof(np.array([]))

print "size of python float:"
print sys.getsizeof(1.0)

print "size of numpy float64:"
print np.array(1.0).itemsize

print "A 1000 element list of floats:"
print 36 + 1000*32 + 1000*16, 'bytes'

print "A 1000 element list of floats:"
print 40 + 1000*8, 'bytes'