#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# The Internet Movie Database (IMDb) is an online collection of information
# about movies. Their database is available in plain text format, so it is
# reasonably easy to read from Python. For this exercise, the files you need
# are actors.list.gz and actresses.list.gz; you can download them from
# www.imdb.com/interfaces#plain.
#
# I have written a program that parses these files and splits them into actor
# names, movie titles, etc. You can download it from
# thinkpython.com/code/imdb.py.
# If you run imdb.py as a script, it reads actors.list.gz and prints one
# actor-movie pair per line. Or, if you import imdb you can use the function
# process_file to, well, process the file. The arguments are a filename, a
# function object and an optional number of lines to process. Here is an
# example:
# import imdb
#
# def print_info(actor, date, title, role):
#    print actor, date, title, role

# imdb.process_file('actors.list.gz', print_info)
#
# When you call process_file, it opens filename, reads the contents, and calls
# print_info once for each line in the file. print_info takes an actor, date,
# movie title and role as arguments and prints them.
# Write a program that reads actors.list.gz and actresses.list.gz and uses
# shelve to build a database that maps from each actor to a list of his or her
# films.
# Two actors are “costars” if they have been in at least one movie together.
# Process the database you built in the previous step and build a second
# database that maps from each actor to a list of his or her costars.
# Write a program that can play the “Six Degrees of Kevin Bacon,” which you
# can read about at wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon. This
# problem is challenging because it requires you to find the shortest path in
# a graph. You can read about shortest path algorithms at
# wikipedia.org/wiki/Shortest_path_problem.

import imdb
import shelve

def store_actor_movie_record(actor, date, title, role) :
    """This function stores an actor movie record"""
    global actor_db

    movie_record = (title, date, role )     # store the date to disambiguate two
                                            # movies with the same name
                                            # For example Mutiny on the
                                            # Bounty was made twice, once in
                                            # 1935 and once in 1962
    actor_db[actor] = actor_db.setdefault( actor, [] ) + [movie_record]
    print actor,"in", title, date, "playing", role


def populate_database(imdb_file) :
    """this function builds a actor database"""

    try :   # There is an empty string in the database which causes an IndexError
        imdb.process_file(imdb_file, store_actor_movie_record)
    except IndexError, e:
        print "imdb.process_file threw a string index error %s.  Giving up on %s and continuing" % \
                ( e, imdb_file )


if __name__ == "__main__" :
# This dictionary is key'd by actor name.  Each key has the value of a list of
# movie titles
# flag=c means open for read and write, creating if need be
# flag=n means open for destructive write (new).  We want to open the shelve file
# for writing because if it already exists, then it is from a run that
# terminated abnormally
    actor_db = shelve.open("movie_db.shelve", flag="n")
    populate_database("actors.list")
    populate_database("actresses.list")
    actor_db.close()




