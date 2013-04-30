
from start import *

# create an array:
a = np.arange(12)
print_info(a)

# reshape it
a.shape = (3,4)
print_info(a)

# transpose it

b = a.transpose()
print_info(b) 

# reshape again
a.shape = (2,2,3)
print_info(a)

# take a slice:
s = a[:,1,:]
print_info(s)