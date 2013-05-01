# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
from start import print_info

# <codecell>

# create an array:
a = np.arange(12)
print_info(a)


# <codecell>

# reshape it
a.shape = (3,4)
print_info(a)


# <codecell>

# transpose it

b = a.transpose()
print_info(b) 


# <codecell>

# reshape again
a.shape = (2,2,3)
print_info(a)


# <codecell>

# take a slice:
s = a[:,1,:]
print_info(s)


# <codecell>

