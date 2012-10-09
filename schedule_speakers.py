#! /usr/bin/env python
#
# This prorgram reads in a list of students from a file, and sorts them in
# random order
#
import sys
import random
import string
import csv

date_students = {0:"Oct 16th", 3:"Oct 23rd", 6:"Oct 30th", 9:"Nov 6th", \
                 12:"Nov 13th", 16:"Nov 20th", 20:"Nov 27th", 24:"Dec 4th",
                  28:"Dec 11th" }
filename = "Student_list.csv"
f = open(filename,"r")
raw_student_list = csv.reader(f, delimiter='\t', quotechar='"')
student_list = []
for a_line in raw_student_list:
# Column 0 is the student last name, Column 1 is the student first name 
# student's name (last name first)
    student_list.append( string.strip( a_line[0]+" "+a_line[1] ) )
random.shuffle( student_list, )
counter = 0
for n in student_list :
    if counter  in date_students.keys() :
        print "----", date_students[counter]
    counter += 1
    print counter, n
print "----"



