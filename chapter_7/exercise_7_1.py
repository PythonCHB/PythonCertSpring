#! /usr/bin/python
#
# From http://greenteapress.com/thinkpython/html/thinkpython008.html
# Chapter 7 exercise 1
# As another example, we can write a function that prints a string n times.
# 
# def print_n(s, n):
#    if n <= 0:
#        return
#    print s
#    print_n(s, n-1)
#
# For this exercise, re-write this function using a loop.

def print_n ( s, n ) :
    for i in range(n) :
        print s


print_n ( "Jeff", 4 )

