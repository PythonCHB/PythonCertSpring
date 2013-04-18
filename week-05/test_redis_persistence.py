#! /usr/bin/env python
#
# This script tests the persistence of a redis database
import redis
import socket   # because we might handle a socket timeout exception
import os
import sys
import subprocess
import random
import time

def check_super_user():
    """This function checks that the process has super user (root) privileges.
This software will only run on UNIX.  It will not run under Cygwin.  I don't
know if this software will run under MS-Windows"""

    egid = os.getegid()
    euid = os.geteuid()

    return egid == 0 and euid == 0
  
def stop_start_redis(op):
    """This function either starts or stops the redis-server daemon, depending
on the value of op.  If op is start, then the daemon is started.  If op is stop
then the daemon is stopped.  If other values are used, then the results are
unpredictable"""
    ret_status = subprocess.call('service redis-server %s' % op, shell=True)
    if ret_status != 0 :
        print "Failed to %s the redis-server" % op
        sys.exit(1)


def test_persistence ( r_server, save=True ):
    # Generate a random string, and see if it is preserved across database calls    
    value = str(random.random())
    print "value is %s" % value

    r_server.set('foo', value)
    if save :
        r_server.save()         # synchronous save - will block until complete
        print "Shutting down the server after saving state"
    else :
        print "Shutting down the server without saving state first"
    stop_start_redis("stop")
    stop_start_redis("start")

    while True:
        print "Waiting for the daemon to start"
        time.sleep(5.0)
        try:
            results = r_server.get('foo')
        except redis.exceptions.ConnectionError:
            print "The daemon isn't accepting connections yet - wait"
        else:
            print "results of the get is %s" % results
            break
    assert results == value, """The value was *not* preserved across daemon
restarts.  save is %s""" % str(save)
    print "The value was preserved across daemon restart. save is %s" % str(save)
    

if __name__ == "__main__" :
    if not check_super_user() :
        print """This program must run with root privileges because it stops and
the restarts the redis server"""
        sys.exit(1)
    # Open a connection to the database
    # r_server = redis.Redis("108.59.89.216", port=6379, db=0)
    r_server = redis.Redis("localhost", port=6379, db=1)

    test_persistence ( r_server, save=True )
    try :
        test_persistence ( r_server, save=False )

    except AssertionError:
        print "The value was not persisted when the state of the database was not saved"

