#! /usr/bin/python
#
# From http://greenteapress.com/thinkpython/html/thinkpython009.html
# Chapter 8 exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

def backwards ( s ) :
    i = len(s)
    while i > 0 :
        print s[i-1]
        i -= 1


backwards ("Jeff")


