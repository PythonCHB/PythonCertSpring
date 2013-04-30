
from start import *

# create an array:
a = np.arange(12)
print_info(a)

# A slice is a view:
b = a[3:6]
print b

b[0] = 44

print b
print a

