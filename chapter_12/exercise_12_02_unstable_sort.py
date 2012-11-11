#! /usr/bin/env python
#
# Exercise 2  
# In this example, ties are broken by comparing words, so words with the same
# length appear in reverse alphabetical order. For other applications you might
# want to break ties at random. Modify this example so that words with the same
# length appear in random order. Hint: see the random function in the random
# module.

import random
random.seed()

def unstable_len_sort ( word_list ) :
    """This function sorts the words in word_list by length.  However, this
function has a tie-breaker: a random number is inserted into the tuple that
is being sorted on"""

    t = []
    for word in word_list :
        t.append( ( len(word), random.random(), word ) )

    t.sort()

    r = []
    for tpl in t :
        r.append( tpl[2] )

    return r

if __name__ == "__main__" :
    t = ["aa", "be", "cc", "def", "feg", "xyzzy", "dogfood" ]
    r = unstable_len_sort ( t )
    print "Given",t,"the sorted list is",r
    
    t = ["oregon", "oregano", "please", "defcd", "fog", "red", "scum" ]
    r = unstable_len_sort ( t )
    print "Given",t,"the sorted list is",r
                  
    t = ["oregon", "thanks", "please", "defacd", "Rachel", "Daniel", "Hoover" ]
    r = unstable_len_sort ( t )
    print "Given",t,"the sorted list is",r
