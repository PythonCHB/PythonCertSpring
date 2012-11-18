#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Exercise 1   Write a program that reads a file, breaks each line into words,
# strips whitespace and punctuation from the words, and converts them to
# lowercase.  Hint: The string module provides strings named whitespace,
# which contains space, tab, newline, etc., and punctuation which contains the
# punctuation characters. Let’s see if we can make Python swear:
#
# >>> import string
# >>> print string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Also, you might consider using the string methods strip, replace and
# translate.

import string
import sys

def process_word ( word ) :
    """This function takes word, reduces it to lowercase, and removes all
punctuation"""
    word = word.lower()
# http://docs.python.org/2/library/stdtypes.html?highlight=translate#str.translate
    word = word.translate( None, string.punctuation+string.whitespace )
    return word
    

def file_to_word_list( filename ) :
    """This function takes all of the text in file filename and returns a list
of all of the words in the file.  All of the words are converted to lower case
and all punctuation is removed.  For example, don't gets converted to dont"""
    f = open(filename, "r" )
    doc_word_list = []
    for line in f :
# split a line of text into words, splitting on space characters
        line_word_list = line.split()
        for word in line_word_list :
            doc_word_list.append ( process_word ( word ) )
    return doc_word_list
        





if __name__ == "__main__" :
    filename = sys.argv[1]
    word_list = file_to_word_list ( filename )
    for word in word_list :
        print word




