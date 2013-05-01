#!/usr/bin/env python

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from start import *

# <codecell>

print "size of empty list:"
print sys.getsizeof([])


# <codecell>

print "size of empty ndarray:"
print sys.getsizeof(np.array([]))


# <codecell>

print "size of python float:"
print sys.getsizeof(1.0)


# <codecell>

print "size of numpy float64:"
print np.array(1.0).itemsize


# <codecell>

print "A 1000 element list of floats:"
print 36 + 1000*32 + 1000*16, 'bytes'


# <codecell>

print "A 1000 element list of floats:"
print 40 + 1000*8, 'bytes'

# <codecell>

