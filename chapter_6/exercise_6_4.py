#! /usr/bin/python
#
# http://greenteapress.com/thinkpython/html/thinkpython007.html
# Exercise 6-4

def b(z):
    prod = a(z, z)
    print z, prod
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print c(x, y+3, x+y)
