#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# To check whether a word is in the word list, you could use the in operator,
# but it would be slow because it searches through the words in order.
# Because the words are in alphabetical order, we can speed things up with a
# bisection search (also known as binary search), which is similar to what you
# do when you look a word up in the dictionary. You start in the middle and
# check to see whether the word you are looking for comes before the word in
# the middle of the list. If so, then you search the first half of the list the
# same way. Otherwise you search the second half.  Either way, you cut the
# remaining search space in half. If the word list has 113,809 words, it will
# take about 17 steps to find the word or conclude that it’s not there.
# Write a function called bisect that takes a sorted list and a target value
# and returns the index of the value in the list, if it’s there, or None if
# it’s not.  Or you could read the documentation of the bisect module and
# use that!

import time


def bisection_search ( lst, target ):
    """This function takes a sorted list lst and a target value and returns
the index of the value in the list, if it’s there, or None if it’s not."""
    list_length = len(lst)
    if list_length == 1:
        if target == lst[0] :
            return 0
        else :
            return None
    ll_over_2 = list_length/2
    result = bisection_search( lst[:ll_over_2], target )
    if result != None :
        return result
    result = bisection_search( lst[ll_over_2:], target )
    if result != None :
        return result+ll_over_2
    return None

def linear_search ( lst, target ) :
    """this function does a linear search of a sorted list, finds the target
valud and returns the location in the list or None if it does not appear"""
    for e in range( len( lst ) ):
        if lst[e] == target :
            return e
    return None

def test_bisection_search( lst, target, correct_answer ):
    assert lst == sorted(lst)          # Verify that the input list is sorted
    result = bisection_search(lst, target)
    if result == correct_answer :
        print "Correct"
    else :
        print "The result is %d but the correct answer is %d" % ( result, \
                            correct_answer)

if __name__ == "__main__" :
    lst = [1, 3, 4, 5, 6, 7, 8, 19]
    test_bisection_search(lst, 3, 1)
    test_bisection_search(lst, 8, 6)
    test_bisection_search(lst, 1, 0)
    test_bisection_search(lst, 4, 2)
    test_bisection_search(lst, 23, None)
    test_bisection_search([1, 2, 3], 3, 2)
    test_bisection_search([1, 2, 3], 2, 1)
    test_bisection_search([1, 2, 3], 1, 0)
    test_bisection_search([1, 2, 3, 4], 3, 2)
    test_bisection_search([1, 2, 3, 4], 4, 3)
    test_bisection_search([1, 2, 3, 4, 5], 5, 4)
    try :
# Test the test_bisection_search function
        test_bisection_search([1, 2, 4, 5, 3], 5, 4)
    except AssertionError:
        print "test_bisection_search detected an out of order list as input"
    
    # words.txt is sorted
    f = open("words.txt", "r")
    word_list = []
    for word in f:
        w = word.rstrip()
        word_list.append( w )
    f.close()
    word_list.sort()
    start_time = time.time()
    print "Looking for word 'coenzymes':", bisection_search(word_list, "coenzymes")
    print "Looking for word 'the':", bisection_search(word_list, "the")
    print "Looking for word 'xyzzy':",  bisection_search(word_list, "xyzzy")
    end_time = time.time()
    print "The recursive bisection search took ", end_time - start_time, "seconds"
    start_time = time.time()
    print "Looking for word 'coenzymes':", linear_search(word_list, "coenzymes")
    print "Looking for word 'the':", linear_search(word_list, "the")
    print "Looking for word 'xyzzy':",  linear_search(word_list, "xyzzy")
    end_time = time.time()
    print "The linear search took ", end_time - start_time, "seconds"
    

    
    
    
    
        
