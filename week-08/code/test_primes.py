#!/usr/bin/env python

"""
test code for factorial code in timing.py
"""

from timing import primes_stupid as primes
#from timing_solution import primes_stupid_4 as primes

def test_1():
    """make sure you get the first one!"""
    assert primes(1) == [2]

def test_2():
    """make sure you get the first one!"""
    assert primes(2) == [2, 3]

def test_3():
    """make sure you get the first one!"""
    assert primes(3) == [2, 3, 5]

def test_5():
    """make sure you get the first one!"""
    assert primes(5) == [2, 3, 5, 7, 11]

def test_12():
    """make sure you get the first one!"""
    assert primes(12) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
