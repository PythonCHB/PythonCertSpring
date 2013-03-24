#! /usr/bin/python
# Chapter 3 exercise 4
"""
A function object is a value you can assign to a variable or pass as an argument.
For example, do_twice is a function that takes a function object as an argument
and calls it twice:
def do_twice(f):
    f()
    f()
Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
    print 'spam'

do_twice(print_spam)
Type this example into a script and test it.
Modify do_twice so that it takes two arguments, a function object and a value,
and calls the function twice, passing the value as an argument.
Write a more general version of print_spam, called print_twice, that takes a
string as a parameter and prints it twice.  Use the modified version of do_twice
to call print_twice twice, passing 'spam' as an argument.
Define a new function called do_four that takes a function object and a value and
calls the function four times, passing the value as a parameter. There should be
only two statements in the body of this function, not four.
"""

def do_twice(f) :
    """Execute function f twice"""

    f()
    f()

def print_spam() :
    """Print the word "spam" """
    print 'spam'

def do_twice_v ( f, v ) :
    """This function executes function f twice with argument v"""
    f(v)
    f(v)

def do_four( f, v ) :
    """Define a new function called do_four that takes a function object and a value and
calls the function four times, passing the value as a parameter. There should be
only two statements in the body of this function, not four."""
    do_twice_v ( f, v )
    do_twice_v ( f, v )

def print_me ( s ) :
    """This function prints the variable s, converting it to a string if necessary"""
    print s

do_twice(print_spam)

do_four( print_me, "baked beans")
do_four( print_me, "Spam" )     # note uppercase S

