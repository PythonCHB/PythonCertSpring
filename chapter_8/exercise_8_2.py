#! /usr/bin/python
#
# From http://greenteapress.com/thinkpython/html/thinkpython009.html
# Chapter 8 exercise 2
#
# In Robert McCloskey's book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, 
# Ouack, Pack, and Quack. This loop outputs these names in order:

#prefixes = 'JKLMNOPQ'
#suffix = 'ack'

#for letter in prefixes:
#    print letter + suffix

# The output is:

#Jack
#Kack
#Lack
#Mack
#Nack
#Oack
#Pack
#Qack

#Of course, that's not quite right because "Ouack" and "Quack" are misspelled.
# Exercise 2  

# Modify the program to fix this error.

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter in 'OQ' :     # This is a trick for strings and other sequences
        letter += 'u'
    print letter + suffix

