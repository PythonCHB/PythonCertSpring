#! /usr/bin/env python
#
#
# This program demonstrates how lambda functions interact with surrounding scopes

glob = 8

f = lambda x: x-glob

print f(2)

glob = 15

print f(3)

def incr(n): return lambda x: x-n
h = incr(2)
i = incr(4)
print h(3), i(3)
print incr(6)(9)

