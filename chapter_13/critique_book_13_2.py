#!  /usr/bin/env python
#
#
# Exercise 13-2  
# Go to Project Gutenberg (gutenberg.org) and download your favorite
# out-of-copyright book in plain text format.
#
# Modify your program from the previous exercise to read the book you
# downloaded, skip over the header information at the beginning of the file,
# and process the rest of the words as before.
# 
# Then modify the program to count the total number of words in the book, and
# the number of times each word is used.
#
#
# Print the number of different words used in the book. Compare different
# books by different authors, written in different eras. Which author uses
# the most extensive vocabulary?

import strip_words_13_1
import sys
import collections    # This includes the Counter class



def file_to_word_list( filename ) :
    """This function takes all of the text in file filename and returns a list
of all of the words in the file.  All of the words are converted to lower case
and all punctuation is removed.  For example, don't gets converted to dont.  This
function also skips through the header.  The end of the header can be recognized
by three asterisks (***) at the beginning of the line"""
# Skip the header
    lc = 0
    f = open(filename, "r" )
    for line in f :
        lc += 1
        # print lc,line[0:3],":", line
        if line[0:3] == "***" :
            break
        
    doc_word_list = []
    for line in f :
# split a line of text into words, splitting on space characters
        line_word_list = line.split()
        for word in line_word_list :
            doc_word_list.append ( strip_words_13_1.process_word ( word ) )
    return doc_word_list

def word_counter ( word_list ) :
    """This function counts the words in word list and returns a Counter object
with the words as the keys and the number of occurances of each word as the
value """
    counter = collections.Counter()
    for word in word_list :
        counter[word] += 1
    return counter
        

if __name__ == "__main__" :
    doc_word_list = file_to_word_list ( sys.argv[1] )
    census = word_counter ( doc_word_list )
    num_of_words = len(census)
    for word in census :
        print word,":",census[word]
    print "There are %d distinct words in %s" % ( num_of_words, sys.argv[1] )
