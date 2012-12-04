#! /usr/bin/env python
#
# This is some examples of a interators

# This is an example from Wesley Chun's book, "Core Python Programming, 2nd ed"
# page 578
class AnyIter(object) :
    def __init__(self, data, safe=False) :
        self.safe=safe
# See http://docs.python.org/2/library/functions.html#iter        
        self.iter = iter(data)

    def __iter__(self) :
        return self

    def next(self, howmany=1):
        """This method returns a list of howmany objects out of data (which was
passed in when the object was instantited) until the list of ojects is exhausted."""
        retval =[]
        for each_item in range(howmany) :
            try :
                retval.append( self.iter.next() )
            except StopIteration :
                if self.safe :
                    break
                else :
                    raise
        return retval

if __name__ == "__main__" :
    d = {"one":1, "two": 2, "three": 3}
    print "The attributes of a dictionary object"
    print dir(d)
    for i in d:
        print i,
    print    

    s = "spam"
    print "The attributes of a string object"
    print dir(s)
    for c in s :
        print c,
    print

    print "Run AnyIter with safe set to false and the list is not exchausted"
    i = AnyIter(range(10), safe=False )
#    i = iter(a)
    for j in range(1,5) :
        print j,":",i.next()

    print "Run AnyIter with safe set to false and the list is exhausted"
#    i = iter(a)
    try :
        i.next(14)
        print j,":",i.next()
    except StopIteration,e :
        print "StopIteration was raised",e
    else :
        print "StopIteration was *not* raised"
        
    print "Run AnyIter with safe set to True and the list is exhausted"
    i = AnyIter(range(10), safe=True)
#    i = iter(a)
    print i.next(14)

    
