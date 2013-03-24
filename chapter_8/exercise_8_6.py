#! /usr/bin/env python
#
#
# Exercise 6   Rewrite this function so that instead of traversing the string,
# it uses the three-parameter version of find from the previous section.
#
# I'm not sure how this is a better version than the version in exercise 8-5,
# because you still have to traverse the string.  You do it either in the caller
# or in the called function, find.

import exercise_8_4    # Get the 3 parameter version of find
# find(word, letter, index)

def count( word, letter ) :
    """Count the number of times the letter letter appears in string word"""
    counter = 0
    i = -1   # Because the call to find increments i by 1, so start at -1 
    while True :
        i = exercise_8_4.find(word, letter, i+1)
        if i == -1 :
# find returns -1 if the letter was not found in word
            break
        counter += 1
    return counter

if __name__ == "__main__" :
    def test_count ( word, letter, expected ) :
        result = count ( word, letter )
        if result == expected :
            print "word %s letter %s produced the expected result %d" % (
                word, letter, result )
        else :
            print "word %s letter %s FAILED! Got %d expected %d" % (
                word, letter, result, expected )

        
    test_count ( 'apple', 'a', 1 )
    test_count ( 'apple', 'b', 0 )
    test_count ( 'apple', 'p', 2 )
    test_count ( 'apple', 'e', 1 )
