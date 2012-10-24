#! /usr/bin/python
# Chapter 4 exercises in sectiib 4.3
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t) :
    """This function uses turtle t yo draw a square"""
    fd(t, 100)
    lt(t)

    fd(t, 100)
    lt(t)

    fd(t, 100)
    lt(t)

    fd(t, 100)

square(bob)

wait_for_user()
