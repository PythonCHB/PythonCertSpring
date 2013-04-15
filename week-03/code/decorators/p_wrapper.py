"""
Python decorator example

simple decorator that turns any function that returns a string
into one that returns that string wrapped in the html <p> tag:

@p_wrapper
def func():
    " simplest example possible"
    return "this is the returned string"

func()

Advanced:

Try using a class to make a decorator that will wrap a
specified tag around a function that returns a string -- i.e:

@tag_wrapper('h1')
def func2(x, y=4, z=2):
    return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

>>> print func2(3,4)
<h1>the sum of 3 and 4 and 2 is 9</h1>


"""

# the simple decorator

def p_wrapper(f):
    """
    fill in decorator here
    """
    pass



# give it a try:
if __name__ == "__main__":

    def func():
        " simplest example possible"
        return "this is the returned string"

    print "the raw version"

    print func()

    # now add the decorator:
    @p_wrapper
    def func():
        " simplest example possible"
        return "this is the returned string"

    print "the decorated version"

    print func()

    # try it with another function

    @p_wrapper
    def func2(x,y):
        return "the sum of %s and %s is %s"%(x, y, x+y)

    # call it:
    print func2(3,4)

    # and one with keyword arguments

    @p_wrapper
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    # call it:
    print func2(3)
    print func2(3, 5)
    print func2(3, 5, 7)


    # ## and try the class version:

    # @tag_wrapper('h1')
    # def func2(x, y=4, z=2):
    #     return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    # print func2(3,4)

    # @tag_wrapper('div')
    # def func2(x, y=4, z=2):
    #     return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    # print func2(5,6,7)

