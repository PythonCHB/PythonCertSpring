# intro to broadcasting:
from start import *

a = np.ones((3,4))

print a * 3

x = np.linspace(0,10,4)
y = np.linspace(100,200,3)

x.shape = (1, -1)
y.shape = (-1, 1)

print x
print y

print a * x
print a * y

print np.sqrt(x**2 * y**2)


