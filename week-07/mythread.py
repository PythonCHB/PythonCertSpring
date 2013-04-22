#! /usr/bin/env python
#
#
import threading
from time import ctime

class My_thread ( threading.Thread ):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)   # intialize the superclass
		self.name = name
		self.func = func
		self.args = args
	
	def run(self):
		print "Starting ", self.name, "at:", ctime()
		self.func ( *self.args )
		print self.name, "finished at", ctime()
		

		def get_result( self ):
			return self.res

    
