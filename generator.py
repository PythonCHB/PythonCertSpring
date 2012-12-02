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

    def a_very_complicated_function(self, x) :
        """This is a very complicated method that does something you probably
won't understand.  For every imput x, it returns an output"""
        return x+1
            
    def generate(self) :
        """This method returns the next value in the series.  It limites the
series to a certain number of values.  Note that this method invokes a
very complicated function"""
        while self.counter < self.end :
            yield self.counter
            self.counter = self.a_very_complicated_function(self.counter)
        raise StopIteration

def generate_1(start, end) :
    """This function demonstrates a generator built as a function"""
    counter = start
    while end > counter :
        yield counter
        counter+=1

def generate_2() :
    yield "Hewey"
    yield "Lewey"
    yield "Dewey"

        

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
    for i in generate_1(2,5) :
        print i

    print "Running the generator function 'echo()'"
    echo_obj = echo(1)
    print echo_obj.next()
    print "Next line should be 'None'"
    print echo_obj.next()
    print "Next line should be 2"
    print echo_obj.send(2)
    print echo_obj.next()    
    try :
        echo_obj.throw(TypeError, "spam")
    except TypeError,e :
        print "The generator object threw a TypeError exception:",e
    print echo_obj.next()
    echo_obj.close()

    print "The attributes of generate_2()"
    print dir(generate_2)
    g = generate_2()
    print "The attributes of g"
    print dir(g)
    print "3 calls to generate_2()"
    print g.next()
    print g.next()
    print g.next()
    try :
        print g.next()
    except StopIteration,e :
        print "StopIteration was raised",e
    else :
        print "Stop Iteration was *not* raised"

        
        
