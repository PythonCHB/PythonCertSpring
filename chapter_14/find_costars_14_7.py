#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Two actors are “costars” if they have been in at least one movie together.
# Process the database you built in the previous step and build a second
# database that maps from each actor to a list of his or her costars.

import shelve

def are_costars( actor_1, actor_2 ) :
    """This function returns True if the two actors both starred in the same
movie, False otherwise"""
    movie_1 = actor_db[actor_1]
    movie_2 = actor_db[actor_2]
# The roles will be different, so we can't just compare tuples    
    return movie_1[0] == movie_2[0] and movie_1[1] == movie_2[1]
        

if __name__ == "__main__" :
# Open the shelve database for reading    
    actor_db = shelve.open("movie_db.shelve", flag="r")

    for actor_1 in actor_db.keys() :
        for actor_2 in actor_db.keys() :
            if are_costars( actor_1, actor_2 ) :
                print actor_1, "and", actor_2, "both appeared in ", \
                      actor_db[actor_1][0], "made in ", actor_db[actor_1][1]
                print actor_1, "portrayed", actor_db[actor_1][2]
                print actor_2, "portrayed", actor_db[actor_2][2]
# If I wanted to do a stretch, then I could put in some code so that if
# actor_1 and actor_2 are co-stars, then it wouldn't list actor_2 and actor_1 as
# costars.  I leave this an exercise for future.



                
