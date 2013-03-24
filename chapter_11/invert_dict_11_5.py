#! /usr/bin/env python
#
# Exercise 5   Read the documentation of the dictionary method setdefault and use
# it to write a more concise version of invert_dict.
# See http://docs.python.org/library/stdtypes.html?highlight=setdefault#dict.setdefault

import efficient_histogram_11_2 as hist

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
# If key is in the dictionary, return its value. If not, insert key with a
# value of default and return default. default defaults to None.        
        inv[val] = inv.setdefault( val, [] ) + [key]
#        if val not in inv:
#            inv[val] =  [key]
#        else:
#            inv[val].append(key)
    return inv

if __name__ == "__main__" :
    while True :
        s = raw_input("Enter a string ")
        h = hist.histogram(s)
        r = invert_dict(h)
        for k in r.keys() :
            print k,":", r[k]
