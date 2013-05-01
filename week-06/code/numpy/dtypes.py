# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# data types
from start import *


# <codecell>

# a custom dtype:
dt = np.dtype([('first_name', np.str_, 16),
               ('last_name',  np.str_, 24),
               ('grades',     np.float64, (2,)),
               ])


# <codecell>

# create an array of this type:

a = np.empty((3,), dtype=dt)


# <codecell>

#Fill it up:
 
a[0] = ('Fred', 'Jones', (92.3, 86.2))    
a[1] = ('Bob', 'Smith', (85.1, 88.4))    
a[2] = ('George', 'Roberts', (76.3, 91.5))    

print_info(a)


# <codecell>

# extract a field:

print a['first_name']


# <codecell>

# do some math on a field:

grades = a['grades']
print grades


# <codecell>

# do some math:
print grades.mean()


# <codecell>

# still a view on the data

print_info(grades) # note the strides!



# <codecell>

