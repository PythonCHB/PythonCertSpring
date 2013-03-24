#! /usr/bin/env python
#
#
# Exercise 4   Modify reverse_lookup so that it builds and returns a list of
# all keys that map to v, or an empty list if there are none.

import efficient_histogram_11_2 as hist
import string

def reverse_lookup(d, v):
    return_list = []
    for k in d:
        if d[k] == v:
            return_list.append(k)
    return return_list

if __name__ == "__main__" :
    while True :
        s = raw_input("Enter a string ")
        h = hist.histogram(s)
        v = 0
        while True :
            rl = reverse_lookup(h, v)
            if ( v > 0 ) and ( len(rl)==0 ) :
                break
            print v, rl
            v += 1
            
