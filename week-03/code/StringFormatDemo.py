# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

fp = 3.4
complex = 3+4j

# <codecell>

print "%f"%(fp)

# <codecell>

print "%f, %f"%(fp, complex)

# <codecell>

print "%f, %f+%fj"%(fp, complex.real, complex.imag)

# <markdowncell>

# But what if you don't know what kind of object you need to format in your string?

# <codecell>

print "%s"%("The string formatter")

# <codecell>

# works for anything...
"%s, %s"%(fp, complex)

# <markdowncell>

# What it does is call the __str__ method on the object.
# 
# There is also "%r" which calls the __repr__ method.

# <codecell>

"%r, %r"%(fp, complex)

# <codecell>

class test(object):
    def __str__(self):
        return "This is the ouput of the __str__ method"
    def __repr__(self):
        return "This is the ouput of the __repr__ method"

# <codecell>

t = test()
"%s"%t

# <codecell>

"%r"%t

# <codecell>


