#! /usr/bin/env python
#
# This prorgram reads in a list of students from a file, and sorts them in
# random order
#
import sys
import random
import string
import csv

date_students = {-1:"Oct 16th", 0:"Oct 23rd", 3:"Oct 30th", 6:"Nov 6th", \
                 9:"Nov 13th", 12:"Nov 20th", 15:"Nov 27th", 18:"Dec 4th",
                  21:"Dec 11th" }
filename = "Student_list.csv"
f = open(filename,"r")
raw_student_list = csv.reader(f, delimiter='\t', quotechar='"')
student_list = []
for a_line in raw_student_list:
# Column 0 is the UW netID, column 1 is the UW student number, column 2 is
# student's name (last name first)
    student_list.append( string.strip( a_line[2] ) )
random.shuffle( student_list, )
counter = 0
for n in student_list :
    if counter  in date_students.keys() :
        print "----", date_students[counter]
    counter += 1
    print counter, n
print "----"



