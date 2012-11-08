#! /usr/bin/env python
#
# Exercise 14-5.  This program demonstrates how to refer to an object on the web
# using the file interface
#
# The urllib module provides methods for manipulating URLs and downloading
# information from the web. The following example downloads and prints a secret
# message from thinkpython.com:
import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn.fp:
    print line.strip()


    
