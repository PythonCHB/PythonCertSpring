#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#
# “Recently I had a visit with my mom and we realized that the two digits that
# make up my age when reversed resulted in her age. For example, if she’s 73,
# I’m 37. We wondered how often this has happened over the years but we got
# sidetracked with other topics and we never came up with an answer.
# “When I got home I figured out that the digits of our ages have been
# reversible six times so far. I also figured out that if we’re lucky it would
# happen again in a few years, and if we’re really lucky it would happen one
# more time after that. In other words, it would have happened 8 times over all.
# So the question is, how old am I now?”

def are_digits_reversed ( v1, v2 ) :
    """Accepts two strings, 2 characters long.  Returns True if the two strings
are reversed, that is, character 1 from 1 string is the same as character 2 from
the other string"""
    return v1[0] == v2[1] and v1[1] == v2[0]

def number_instances ( diff ) :
    """Returns the number of times the digits are reversed given the differnce
in the ages"""
    child = 0
    age_list = []
    while True :
        parent = child + diff
        parent_age_str = "%02d" % parent
        child_age_str = "%02d" % child
        if are_digits_reversed ( parent_age_str, child_age_str ) :
            age_list.append(child)
        if parent > 99 :
            break
        child += 1
    return age_list

print "Diff\t#instances"
for diff in range ( 10, 70 ) :      # seems unlikely that the mother would be 10...
    age_list = number_instances ( diff )
    if len(age_list) > 0 :
        print "%d\t%d" % (  diff, len(age_list) )
    if len(age_list) == 8 :
        print "I am currently %d years old and my parent is %d years olf" \
              % ( age_list[5], age_list[5]+diff )
        
        
