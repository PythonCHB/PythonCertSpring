# data types
from start import *

# a custom dtype:
dt = np.dtype([('first_name', np.str_, 16),
               ('last_name',  np.str_, 24),
               ('grades',     np.float64, (2,)),
               ])

# create an array of this type:

a = np.empty((3,), dtype=dt)

#Fill it up:
 
a[0] = ('Fred', 'Jones', (92.3, 86.2))    
a[1] = ('Bob', 'Smith', (85.1, 88.4))    
a[2] = ('George', 'Roberts', (76.3, 91.5))    

print_info(a)

# extract a field:

print a['first_name']

# do some math on a field:

grades = a['grades']
print grades

# do some math:
print grades.mean()

# still a view on the data

print_info(grades) # note the strides!


