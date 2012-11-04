#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercise 11-1
# Write a function that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.
#
# If you did Exercise 10.8, you can compare the speed of this implementation
# with the list in operator and the bisection search.


# http://www.greenteapress.com/thinkpython/html/book011.html#wordlist1
import bisection_search_10_8 as bisect
import random
import time

word_list = []
word_dict = {}

def populate_word_list() :
    global word_list
    global word_dict
    f = open("words.txt", "r")
    word_list = []
    for word in f:
        w = word.rstrip()
        word_list.append( w)
        word_dict[w]=1        # We don't care what the value is
    f.close()

def dictionary_search( my_word_list ) :
    """Use the dictionary membership test to see if each word in my_word_list is
in dictionary word_dict"""
    global word_dict # not needed here, but why is it a good idea anyway?
    for word in my_word_list :
        _ = word in word_dict


def list_membership_search( my_word_list ) :
    """Use the  list membership test to see if each word in my_word_list is
in dictionary word_dict"""
    global word_list # not needed here, but why is it a good idea anyway?
    for word in my_word_list :
        _ = word in word_list
            
def bisection_search ( my_word_list ) :
    """Use the bisection search test we wrote in chapter 10 to see if each
word in my_word_list is in the list word_list"""
    global word_list
    for word in my_word_list :
        _ = bisect.bisection_search ( word_list, word )
 
if __name__ == "__main__" :
    NUM_SAMPLES = 1000
    populate_word_list()
    sample_word_list = random.sample ( word_list, NUM_SAMPLES )
    
    start=time.time()
    dictionary_search( sample_word_list )
    print "Dictionary search took %f seconds" % ( time.time() - start )

    start=time.time()
    bisection_search( sample_word_list )
    print "bisection search took %f seconds"% (time.time() - start )

    start=time.time()
    list_membership_search( sample_word_list )
    print "list membership search took %f seconds" % ( time.time() - start )
    





