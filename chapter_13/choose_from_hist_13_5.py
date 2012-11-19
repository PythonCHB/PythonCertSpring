#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercise 13-5  
# Write a function named choose_from_hist that takes a histogram as defined in
# Section 11.1 and returns a random value from the histogram, chosen with
# probability in proportion to frequency. For example, for this histogram:
#
# >>> t = ['a', 'a', 'b']
# >>> h = histogram(t)
# >>> print h
# {'a': 2, 'b': 1}
# your function should ’a’ with probability 2/3 and 'b' with probability 1/3.
#
import random
import collections

PROOF_OF_CONCEPT = False

def histogram(s):
    d = collections.Counter()
    for c in s:
        d[c]+=1
    return d

t = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'd', 'd']

h = histogram(t)
print h


# I got this answer from Stackoverflow.  I thought that the solution would be
# a list with a variable number of elements.  This is a very efficient way
# to generate such a list using a generator comprehension in a lambda function
# http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
# The probolem with this approach is that I am using a list to create a dictionary
# (really a counter

if PROOF_OF_CONCEPT :
    weighted_choice = lambda s : random.choice(sum(([v]*wt for v,wt in s.iteritems()),[]))
else :
    def weighted_choice( s ):
        w = [[v]*wt for v, wt in s.iteritems()]
        return random.choice(sum(w,[]))

# initialize tally dict
#    tally = dict((c[0],0) for c in h)
tally = collections.Counter() 

# tally up 10000 weighted choices
for i in xrange(10000):
    tally[weighted_choice(h)] += 1

print tally.items()
