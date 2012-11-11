#! /usr/bin/python
#
# From: http://greenteapress.com/thinkpython/html/thinkpython009.html
# modify the find function so that it takes a third paratmeter, index, where it
# should start looking.

def find(word, letter, index) :
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

if __name__ == "__main__" :
    def test_find ( word, letter, index, expected ) :
        result = find ( word, letter, index )
        if result == expected :
            print "word %s letter %s index %d produced the expected result %d" % (
                word, letter, index, result )
        else :
            print "word %s letter %s index %d FAILED! Got %d expected %d" % (
                word, letter, index, result, expected )

        
    test_find ( 'apple', 'a', 0, 0 )
    test_find ( 'apple', 'a', 1, -1 )
    test_find ( 'apple', 'b', 0, -1 )
    test_find ( 'apple', 'p', 1, 1 )
    test_find ( 'apple', 'w', 3, -1 )
    test_find ( 'apple', 'p', 17, -1 )
    test_find ( 'apple', 'e', 3, 4 )

