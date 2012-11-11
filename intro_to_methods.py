#! /usr/bin/python
#
#
# intro_to_methods.py
#
class F(object):
    def f(self,x) :
        self.x = x
    def p(self) :
        print self.x

    def __str__(self):
        return str(self.x)
        

f = F()
try :
    print f.x
except AttributeError, e:
    print "I guess you can't do that: " + str(e)
f.f(4)
f.p()
print str(f)

