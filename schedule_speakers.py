#! /usr/bin/env python
#
# This prorgram reads in a list of students from a file, and sorts them in
# random order
#
import sys
import random
import string

filename = "student_list.txt"
f = open(filename,"r")
student_list = []
for l in f:
    student_list.append( string.strip( l ) )
random.shuffle( student_list, )
counter = 0
print "----"
for n in student_list :
    counter += 1
    print counter, n
    if counter  in [3, 6, 9, 12, 16, 20, 24, 28, 32] :
        print "----"



