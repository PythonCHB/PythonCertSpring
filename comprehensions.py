#! /usr/bin/env python
#
# demonstration of list comprehension vs. generator comprehension in a loop 
import math

for i in [x for x in range(100) if math.sqrt(x) % 1.0 == 0 ] :
    print i,
print

for i in (x for x in range(100) if math.sqrt(x) % 1.0 == 0 ) :
    print i,
print

S = [x for x in range(100) if math.sqrt(x) % 1.0 == 0 ]
G = (x for x in range(100) if math.sqrt(x) % 1.0 == 0 )

print type(S)
for i in S :
    print i,
print

print type(G)
for i in G :
    print i,
print
