# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


# intro to broadcasting:
from start import *


# <codecell>

a = np.ones((3,4))


# <codecell>

print a * 3


# <codecell>

x = np.linspace(0,10,4)
y = np.linspace(100,200,3)

x.shape = (1, -1)
y.shape = (-1, 1)

print x
print y

# <codecell>

print a * x
print a * y


# <codecell>

print np.sqrt(x**2 * y**2)


# <codecell>


