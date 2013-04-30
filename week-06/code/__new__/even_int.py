#!/usr/bin/env python

"""
Using new to create an always-positive even integer

rounds the input to the nearest even integer.

will even convert a string to an int...

"""

##subclassing an int

class EvenInt(int):
    """
    An integer that is always even
    """
    pass

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

