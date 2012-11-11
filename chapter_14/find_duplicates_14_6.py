#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#
# In a large collection of MP3 files, there may be more than one copy of the
# same song, stored in different directories or with different file names. The
# goal of this exercise is to search for these duplicates.
#
# Write a program that searches a directory and all of its subdirectories,
# recursively, and returns a list of complete paths for all files with a given
# suffix (like .mp3). Hint: os.path provides several useful functions for
# manipulating file and path names.  To recognize duplicates, you can use a
# hash function that reads the file and generates a short summary of the
# contents. For example, MD5 (Message-Digest algorithm 5) takes an
# arbitrarily-long “message” and returns a 128-bit “checksum.” The probability
# is very small that two files with different contents will return the same
# checksum.

# You can read about MD5 at wikipedia.org/wiki/Md5. On a Unix system you can
# use the program md5sum and a pipe to compute checksums from Python.

# The data structure I picked for this implementation was a directory keyed by
# MD5 sum and which contains a list of files with the same checksum
#
# http://docs.python.org/2/library/md5.html
import md5   # Note that this is portable across operating systems, while spawning
             # a subprocess has portability issues
import os
import sys


def walk_files ( root_dir ) :
    md5_dict = {}
    for root, sub_folders, files in os.walk(root_dir):
        if sub_folders != [] :
            for folder in sub_folders:
                folder_path = os.path.join(root, folder )
                print "Entering directory %s" % folder_path
# According to http://docs.python.org/2/library/os.path.html, os.path.join automatically picks the right
# os.sep
# YOU CANNOT ADD TO DICTIONARIES TOGETHER.  FIND OUT HOW TO CONCATENATE DICTIONARIES
                md5_dict += walk_files( folder_path )
        else :
            for filename in files:
                try :
                    file_path = os.path.join(root,filename)
                    print "Proessing %s" % file_path
                    f = open(file_path,"rb")     # mp3 files are binary
                    file_contents = ''.join ( f.readlines()  )  # read the entire file into
                    # RAM.  The result of readlines is a list, so join them with no
                    # separator
                    m = md5.new( file_contents )
                    md5_sum = m.hexdigest()
                    md5_dict[md5_sum] = md5_dict.setdefault(md5_sum,[]) + [file_path]
                except IOError, e :
                    print "Exeception IOError was raised %s", e
        
    return md5_dict        

rootdir = sys.argv[1]
md5_dict = walk_files (rootdir)

for md5_sum in md5_dict :
    file_list = md5_dict[md5_sum]
    if len(file_list) > 1 :
        print "The following files are duplicates", file_list

