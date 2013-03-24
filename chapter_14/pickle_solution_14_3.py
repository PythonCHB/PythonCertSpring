#! /usr/bin/env python
#
#
# Exercise 12-3
# If you did Exercise 12.4, modify your solution so that it creates a database
# that maps from each word in the list to a list of words that use the same set
# of letters.
# Write a different program that opens the database and prints the contents in
# a human-readable format.


import pickle



# I decided that rather than import exercise 12-3, I would copy and paste it
# here.
word_list = []

def initialize_word_list() :
    """This subroutine initializes the list of words.  If a word is in this list,
then it is a word"""
    global word_list
    f = open("words.txt","r")
    for line in f:
         word = line.strip()
         word_list.append ( word )
    f.close()

def string_to_tuple( word ) :
    """Convert string word into a tuple suitable for use as a key to a dictionary
of anagrams"""
    this_word_list = list(word)     # convert the string to a list so we can sort it
    this_word_list.sort()
    this_word_tuple = tuple( this_word_list )   # Conver the list to a tuple which can be the key to a dictionary
    return this_word_tuple

def make_dict_of_anagrams ( ) :
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
    initialize_word_list()
    anagram_dict=make_dict_of_anagrams()
    f=open("anagrams.pickle", "w")
    pickle.dump(anagram_dict, f, pickle.HIGHEST_PROTOCOL)
    f.close()
    print "The anagram dictionary has been pickled"

if __name__ == "__main__" :
    main()
    
