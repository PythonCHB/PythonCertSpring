#! /usr/bin/python
# Chapter 4 exercises in section 4.3
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t, length) :
    """This function uses turtle t to draw a square"""
    for i in range(4) :
        fd(t, length)
        lt(t)

square(bob, 100)
square(bob, 150)
square(bob, 75)

wait_for_user()
