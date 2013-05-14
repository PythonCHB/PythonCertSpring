#!/usr/bin/env python

"""
NOTE: common wisdom is don't build up strings by adding.
      rather, build in a list, then .join()

But time these to see the actual difference!

"""

def build1(N):
    a_string = 'something'
    string = ""
    for i in xrange(N):
        string += a_string
    return string


def build2(N):
    a_string = 'something'
    string = []
    for i in xrange(N):
        string.append(a_string)
    return "".join(string)



