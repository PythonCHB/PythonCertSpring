#!/usr/bin/env python
"""
script to start up demo for numpy talk
"""

import numpy as np
import sys

def print_info(a):
    print "a:"
    print a
    print "a.shape:", a.shape
    print "a.dtype:", a.dtype
    print "a.itemsize", a.itemsize
    print "a.ndim:", a.ndim
    print "a.strides", a.strides
    print "a.flags:\n", a.flags
    

