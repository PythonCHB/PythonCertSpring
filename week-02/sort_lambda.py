#! /usr/bin/env python
#
# This program demonstrates the use of the lambda function to sort a list of
# tuples
#
#
my_list = [('one',2,['eggs','cheese']),
           ('seventeen',17,['oregano','paparika']),
           ('six',6,['steak','lobster']),
           ('twelve',12,['beer','soda'])]

print "Before", my_list
my_list.sort(key=lambda x: x[1])
print "\nAfter", my_list

           

