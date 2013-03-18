#! /usr/bin/env python
"""This software traverses the web and loads the data into a redis database
The key to the database is a URL, the values of the keys are a list of
outbound urls.  If the url has already been visited, then it is skipped"""

from bs4 import BeautifulSoup
import redis
import time
import urllib2
import socket   # because we might handle a socket timeout exception

VISITED_LIST = "redis_demo_bs_spider_visited_list"  # keyname of the visited list
TO_VISIT_SET = "redis_demo_bs_spider_to_visit_set"  # keyname of the set of pages
                                                    # to visit
# Open a connection to the database
# r_server = redis.Redis("108.59.89.216", port=6379, db=0)
r_server = redis.Redis("localhost", port=6379, db=0)


# Clear out the keys in the database that hold the list of sites that we have visited
# and the set of sites to visit.
r_server.delete(VISITED_LIST )
r_server.delete(TO_VISIT_SET )
# Insert all the specified values at the tail of the list stored at key. If key
# does not exist, it is created as empty list before performing the push
# operation.  Start at commercialventvac.com, which is well connected.
r_server.sadd(TO_VISIT_SET, "http://www.commercialventvac.com")
start_time = time.time()
while time.time() < start_time + 120.0:  # 15.0 seconds
# Removes and returns a random element from the set value stored at key.
    this_page = r_server.spop(TO_VISIT_SET)
    print "**** Crawling %s visited %d " % ( this_page, r_server.llen( VISITED_LIST ))
    try:
        response = urllib2.urlopen(this_page, timeout=15)    # timeout is in seconds
    except (urllib2.URLError, socket.timeout, ValueError),e:
        print "The URL %s failed due to %s - skipping" % ( this_page, e)
        continue
    
    html_doc = response.read()
# Push this_page to the end of the visited list    
    r_server.rpush(VISITED_LIST, this_page)
    soup = BeautifulSoup(html_doc, "html5lib")
    link_list = soup.find_all('a')
    for link in link_list:
        if 'href' in link.attrs :
            url = link.attrs['href']
        
    # This is necessary because if this key already exists and it is not a set
    # type, then the sadd command throws a
    # "Operation against a key holding the wrong kind of value"
    # This is a leftover from previous runs of this software, which used a different
    # data structure
            if r_server.exists(url) :
    # Returns the string representation of the type of the value stored at key. The
    # different types that can be returned are: string, list, set, zset and hash.            
                if r_server.type(url) != "set" :
                    r_server.delete(url)
    # Add the url to the set of urls that we need to visit.  If the URL is already
    # in the set, then this doesn't do anything.
            r_server.sadd(TO_VISIT_SET, url)
            r_server.sadd(this_page, url)
            

while r_server.llen(VISITED_LIST) > 0:
# Get the next URL in the list of URLs that we visited  
    url = r_server.lpop(VISITED_LIST)
# is the set of links that URL points to empty?
    while r_server.scard(url) > 0 :
        link = r_server.spop(url)
        print "%s => %s"% ( url, link )
    

