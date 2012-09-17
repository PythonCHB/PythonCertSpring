#! /usr/bin/python
#
# This program demonstrates scope rules

x=1

def f ( y ) :
  z = x + y		# global variable already exists, can be referenced
  return z

def g ( ) :
  global x		# explicitly added to scope
  x = x + 1

def h ( y ):
  x = 4 + y		# Create a new x in the local scope
  print "In h: x=", x

def epic_fail ( w ) :
  x = x + w		# So why does this fail?
  return x


a = f(2)
print a
g()
print x
h(3.7)
print "After h: x=", x
q = epic_fail ( 6 )
print q


