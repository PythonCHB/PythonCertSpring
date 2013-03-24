#! /usr/bin/env python
"""This software traverses the web and loads the data into a redis database
The key to the database is a URL, the values of the keys are a list of
outbound links.  If the link has already been visited, then it is skipped"""

import chilkat
import redis

# Open a connection to the database
r_server = redis.Redis("localhost")

#  The Chilkat Spider component/library is free.
spider = chilkat.CkSpider()

#  The Initialize method may be called with just the domain name,
#  such as "www.joelonsoftware.com" or a full URL.  If you pass only
#  the domain name, you must add URLs to the unspidered list by calling
#  AddUnspidered.  Otherwise, the URL you pass to Initialize is the 1st
#  URL in the unspidered list.
spider.Initialize("www.commercialventvac.com")

spider.AddUnspidered("http://www.commercialventvac.com/")

visited_list = []
for ctr in range(0,10000):  # This should be limited by something.
    success = spider.CrawlNext()
    this_page = spider.lastUrl()
# This is necessary because if this key already exists and it is not a list
# type, then the rpush command throws a
# "Operation against a key holding the wrong kind of value"
# The kludge is to delete the key if it exists
    if r_server.exists(this_page) :
        try:
            v = r_server.get(this_page)
            print "%s is already in the database, and it is of type %s and contains %s" %\
                ( this_page, type(v), v )
            r_server.delete(this_page)
        except redis.exceptions.ResponseError,e:
            print "Deleting the key %s caused exception %s of type %s" %\
                ( this_page, e, type(e) )
    visited_list.append(this_page)
    print "**** Crawling %s "% this_page
    for i in range(0,spider.get_NumOutboundLinks()):
        link = spider.getOutboundLink(i)
        r_server.rpush(this_page, [link])
        print link,
        if r_server.exists(link):
            print "has been seen before"
        else:
            print "is new"
            spider.AddUnspidered( link )


for page in visited_list :
# http://redis.io/commands#list    
    referenced_pages_list = r_server.lrange(page, 0, -1)
    print "The pages from %s are:" % page
    for ref_page in referenced_pages_list :
        print " "*5,ref_page


