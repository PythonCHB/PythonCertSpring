#! /usr/bin/python
#
#
s = "Level 0\n\tLevel 1\n\t\tLevel 2"
print s

# raw string, note the leading r
r = r"Level 0\n\tLevel 1\n\t\tLevel 2"
print r

# Regular expressions with delimited strings
re_1 = "\\w\\d{2,3}"
print re_1

re_2 = r"\w\d{2,3}"
print re_2
