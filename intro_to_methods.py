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

f = F()
f.f(4)
f.p()
