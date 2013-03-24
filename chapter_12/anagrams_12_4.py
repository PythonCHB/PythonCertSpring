#! /usr/bin/env python
#
#
# Exercise 12-4.  Write a program that creates a databases of anagrams



def initialize_word_list() :
    """This subroutine initializes the list of words.  If a word is in this list,
then it is a word"""
    word_list = []
    f = open("words.txt","r")
    for line in f:
         word = line.strip()
         word_list.append ( word )
    f.close()
    return word_list

def string_to_tuple( word ) :
    """Convert string word into a tuple suitable for use as a key to a dictionary
of anagrams"""
    this_word_list = list(word)     # convert the string to a list so we can sort it
    this_word_list.sort()
    this_word_tuple = tuple( this_word_list )   # Conver the list to a tuple which can be the key to a dictionary
    return this_word_tuple

def make_dict_of_anagrams ( word_list ) :
    """This function returns a dictionary of lists of words which are anagrams.
The keys to the dictionaries are tuples of the letters in the words, sorted"""
    anagram_dict = dict()
    for word in word_list:
        this_word_tuple = string_to_tuple ( word )
    # If key is in the dictionary, return its value. If not, insert key with a
    # value of default and return default. default defaults to None.
    # See exercise 11-2
        anagram_dict[this_word_tuple] = \
                        anagram_dict.setdefault( this_word_tuple, [] ) + [word]
    return anagram_dict

def main() :
    word_list = initialize_word_list()
    anagram_dict=make_dict_of_anagrams( word_list )
    i = 0
    for word in word_list :
        key = string_to_tuple(word)
        anagram_list = anagram_dict[key]
# if there are anagrams, then print them.  Most words have no anagrams        
        if len ( anagram_list ) > 1 :
            print anagram_list
            i += 1
            if i > 200 : # I just want 200 anagrams as a proof of concept
                break
# Part 2 of the problem: output the list sorted by length
    anagram_list_length_list = []
    for key in anagram_dict.keys() :
        anagram_list_length_list.append( (len(anagram_dict[key]), key) )
    anagram_list_length_list.sort()
    for i in range( len ( anagram_list_length_list ) ) :
        key = anagram_list_length_list[i][1]
        anagram = anagram_dict[key]
        if len(anagram) > 1 :
            print anagram
#

if __name__ == "__main__" :
    main()

    
