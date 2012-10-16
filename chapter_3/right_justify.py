#! /usr/bin/python
# Chapter 3 exerise 3

def right_justify(s, align_column=70) :
    """Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the string is
n column 70 of the display."""
    len_s = len(s)
    leading_spaces = align_column - len_s
# The careful student will understand the difference between using a comma and a plus
# sign here
    print " "*leading_spaces + s

print "70"
print "."*70
right_justify("Allen")

print "60"
print "."*60
right_justify("Silverman",60)

print "10"
print "."*10
right_justify("Sarah",10)

