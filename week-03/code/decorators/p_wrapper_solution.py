"""
Python decorator example

simple decorator that turns any function that returns a string
into one that returns that string wrapped in the html <p> tag:

@p_wrapper
def func():
    " simplest example possible"
    return "this is the returned string"

func()

"""

# the simple decorator

def p_wrapper(f):
    def function(*args, **kwargs):
        result = f(*args, **kwargs)
        return "<p>" + result + "</p>"
    return function

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

