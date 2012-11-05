#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Two words form a “metathesis pair” if you can transform one into the other by
# swapping two letters; for example, “converse” and “conserve.” Write a program
# that finds all of the metathesis pairs in the dictionary. Hint: don’t test all
# pairs of words, and don’t test all possible swaps.

# First of all, all metathesis pairs are anagrams, so if two words are not
# anagrams, they can be rejected.

# http://epequeno.wordpress.com/2011/12/27/exercise-12-04/

import anagrams_12_4

def num_differences ( word_1, word_2 ) :
    """This function calculates how many characters differ between word_1 and
word_2"""
    count = 0
    for i in range(len(word_1)) :
        if word_1[i] != word_2[i] :
            count += 1
    return count 

if __name__ == "__main__" :
# Get a list of words from a file.
    word_list = anagrams_12_4.initialize_word_list()
# Create a dictionary of anagrams.  The dictionary is keyed by tuples
# and has a list of anagrams for values.  The tuples are the letters in the word
# sorted.  You never actually use the keys, they are opaque identifiers
    anagram_dict=anagrams_12_4.make_dict_of_anagrams( word_list )

# Loop over all lists of anagrams.  itervalues returns an iterator over the
# values in the dictionary.  We could have done the same thing with
# for k in anagram_dict.keys()
#    anagram = anagram_dict[key]
# 
    for anagram in anagram_dict.itervalues() :
        for word_1 in anagram :
            for word_2 in anagram :
# Two anagramic words can be a metathesis pair if the number of characters that
# differ between them are 2.
                differences = num_differences( word_1, word_2 )
# Making sure that we only print when word_1 > word_2 eliminates duplicates
                if differences == 2 and word_1 > word_2 :
                    print word_1, word_2


                    
                
    




