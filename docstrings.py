#! /usr/bin/python
#
# Demonstrates how to document a very confusing function

def confusion ( a, b, c ) :
  """This is a very confusing function and you are wise to read the documentation
for it.
a is the first argument
b is the second argument
c is the third argument
"""
  return ( a,b,c )


print help(confusion)
print "*" * 30
print confusion.__doc__


