# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## keyword argument scope demo

# <markdowncell>

# Define a variable in the global scope:

# <codecell>

a = 5

# <markdowncell>

# Use that variable in a function:

# <codecell>

def add(x):
    return x + a

# <markdowncell>

# call the function -- a is used:

# <codecell>

add(3)

# <markdowncell>

# change a

# <codecell>

a = 12

# <codecell>

add(3)

# <markdowncell>

# The new a is used

# <markdowncell>

# But what if I don't want the results to depend on what a gets re-set to.
# 
# But I don't want a constant, either...
# 
# Set a keyword argument:

# <codecell>

def add(x, a=a):
    return x + a

# try it:
add(3)

# <markdowncell>

# it used the last value.
# 
# reset a

# <codecell>

a = 100
add(3)

# <markdowncell>

# Still used the original value!

# <markdowncell>

# ## Lesson:
# 
# The keyword arguments are evaluted _when the function is defined, NOT when it is called.

# <codecell>


