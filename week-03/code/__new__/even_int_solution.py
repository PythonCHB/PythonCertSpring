#!/usr/bin/env python

"""
Using new to create an always-positive even integer
"""

##subclassing an int

class EvenInt(int):
    """
    A string class that is always capitalized...
    """
    def __new__(cls, val):
        print "in EvenInt.__new__", val
        val = round(float(val) / 2) * 2
        print val
        return int.__new__(cls, val )


## And some tests -- try with py.test or nosetests...

def test_subclass():
    assert issubclass(EvenInt, int)

def test_instance():
    i = EvenInt(3)
    assert isinstance(i, int)

def test_even():
    assert EvenInt(4) == 4

def test_odd1():
    assert EvenInt(3) == 4

def test_odd2():
    assert EvenInt(2.99) == 2

def test_negative():
    assert EvenInt(-2) == -2

def test_negative_odd():
    assert EvenInt(-1) == -2

def test_negative_odd2():
    assert EvenInt(-1.1) == -2

def test_string_odd():
    assert EvenInt("3") == 4

def test_string_even():
    assert EvenInt("12") == 12



