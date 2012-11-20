# Name: 

"""
Quiz  Week 2

By each numbered comment, write the value of the expression that appears on that line
(that would be printed if you typed the expression in an interactive session).
If the expression (or its predecessor) is erroneous (could not be evaluated),
 just write "error" or a big "X"
If you don't know the value, just write "?" or leave it blank.
"""

# Parameter passing, scope

x = 1

def f(x):
    return 2*x

f(x)   # 1.
x      # 2.

def g(x):
    x = 2*x
    return x

g(2*x)  # 3.
x       # 4.

# Definition and use

def p(x):
    return 2*f(2*x)

p(x)    # 5.

def q(x):
    return 2*r(x)

q(x)    # 6.
