#! /usr/bin/env python
#
#
#  The os module provides a function called walk that is similar to this one
# but more versatile. Read the documentation and use it to print the names of
# the files in a given directory and its subdirectories.
#
# See http://docs.python.org/library/os.html#files-and-directories

import os

# you should understand the difference between walk and os.walk
def walk ( directory ) :
    "Return a list of all the files in the directory tree directory"
    file_list = []
    for root, dirs, files in os.walk(directory, topdown=True, onerror=None ):
        for f in files :
# os.sep is the path element separator.  It is / for unix and Mac OS X, \ for
# MS-DOS, and . for OpenVMS.
            file_list.append( root+ os.sep + f )
    return file_list

if __name__ == "__main__" :
    root = raw_input("Enter the directory you want to list ")
    file_list = walk( root )
    print file_list
