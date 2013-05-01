# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


import numpy as np
from start import *


# <codecell>

# create an array:
a = np.arange(12)
print_info(a)


# <codecell>

# A slice is a view:
b = a[3:6]
print b
print_info(b, 'b')


# <codecell>

# note "OWNDATA" flag -- b does not "own" its data.

b[0] = 44

print b
print a

# a has changed!


# <codecell>

# what about slicing higher-dim arrays:
a = np.arange(12).reshape(3,4)
print_info(a,'a')


# <codecell>

# "row" slice:
b = a[1,:]
print_info(b,'b')


# <codecell>

# "column" slice:
b = a[:,1]
print_info(b,'b')


# <codecell>

