#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercise 17-6  
# This exercise is a cautionary tale about one of the most common, and difficult
# to find, errors in Python.
# Write a definition for a class named Kangaroo with the following methods:
# An __init__ method that initializes an attribute named pouch_contents to an
# empty list.
# A method named put_in_pouch that takes an object of any type and adds it to
# pouch_contents.
# A __str__ method that returns a string representation of the Kangaroo object
# and the contents of the pouch.
# Test your code by creating two Kangaroo objects, assigning them to variables
# named kanga and roo, and then adding roo to the contents of kanga’s pouch.

class Kangaroo( object ) :

    def __init__ ( self ):
        self.pouch_contents = []

    def put_in_pouch(self, o ):
        self.pouch_contents.append(o)

    def __str__ ( self ):
        return "pouch contains "+ str(self.pouch_contents)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print kanga
print roo
kanga.put_in_pouch("lipstick")
kanga.put_in_pouch("Mascara")
roo.put_in_pouch("Pens")
roo.put_in_pouch("Cell phone")
print "kanga= ",kanga
print "roo= ",roo


        
    
