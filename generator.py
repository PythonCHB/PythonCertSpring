#! /usr/bin/env python
#
#

class Jeffs_generator(object):
    """This class demonstrates a generator built as a class
A generator creates a next method and raises the StopIteration exception when
it is done iterating"""
    def __init__ ( self, end, start=0 ) :
        assert end >= start,"end should be greater than start"
        self.counter=start
        self.end=end

    def generate(self) :
        while self.counter < self.end :
            yield self.counter
            self.counter+=1
        raise StopIteration

def generate(start, end) :
    """This function demonstrates a generator built as a function"""
    counter = start
    while end > counter :
        yield counter
        counter+=1

# Here is an example from the Python documentation
# http://docs.python.org/2/reference/expressions.html#yieldexpr
def echo(value=None):
    print "Execution starts when 'next()' is called for the first time."
    try:
        while True:
            try:
                value = (yield value)
            except Exception, e:
                value = e
    finally:
        print "Don't forget to clean up when 'close()' is called."




if __name__ == "__main__" :
    j = Jeffs_generator(8,4)
    print "Using a generator function defined in a class"
    for i in j.generate() :
        print i

    print "Using a generator function"
    for i in generate(2,5) :
        print i

    
    generator_obj = echo(1)
    print generator_obj.next()
    print "Next line should be 'None'"
    print generator_obj.next()
    print "Next line should be 2"
    print generator_obj.send(2)
    print generator_obj.next()    
    try :
        generator_obj.throw(TypeError, "spam")
    except TypeError,e :
        print "The generator object threw a TypeError exception:",e
    print generator_obj.next()
    generator_obj.close()



