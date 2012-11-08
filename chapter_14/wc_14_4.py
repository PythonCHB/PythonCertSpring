#! /usr/bin/env python
#
# Use this program as both a script and as a module in a larger program
import sys
import os

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if __name__ == "__main__" :
    for arg in sys.argv :
        if not os.path.isdir(arg) :
                lc = linecount ( arg )
                print arg, ":", lc
else :
    print "The name of this module is %s" % __name__
    
