#! /usr/bin/env python
#
#
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.
# Modify print_hist to print the keys and their values in alphabetical order.

import efficient_histogram_11_2 as hist

def print_hist(h):
    key_list = h.keys()
    key_list.sort()
    for c in key_list :
        print c, h[c]

if __name__ == "__main__" :
    while True :
        s = raw_input("Enter a string ")
        h = hist.histogram(s)
        print_hist(h)
