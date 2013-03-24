#! /usr/bin/env python
#
#
# Exercise 1   Modify walk so that instead of printing the names of the files, it
# returns a list of names.

import os

def walk(directory):
    "Return a list of all the files in the directory tree directory"
    file_list = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        if os.path.isfile(path):
            file_list.append(path)
        else:
            file_list + walk(path)
    return file_list

if __name__ == "__main__" :
    root = raw_input("Enter the directory you want to list ")
    file_list = walk( root )
    print file_list

