#! /usr/bin/env python

# This program demonstrates that using processes does improve the execution
# time of a multiprocess program
from multiprocessing import Process
from time import time, ctime
import os

iterations = [4, 2, 7]
scaling_factor = 100000000 # Change this number so that the subprocess takes a
                            # reasonable amount of time.  CPU dependent



for i in range(len(iterations)):
    iterations[i] *= scaling_factor

def loop(nloop, iterations):
        start_time = time()
	print 'start loop', nloop, 'at:', ctime(), 'PID is ', os.getpid()
	l = 0.0
	for i in xrange(iterations):
            l += 1.0
	print 'loop', nloop, 'done at:', ctime(),'Elapsed time is %f seconds' % (time()-start_time) 

def main():
	start_time = time()
	print 'starting at:', ctime(), 'PID is', os.getpid()
	processes = []
	n_iterations = range(len(iterations))

	for i in n_iterations:
		p = Process(target=loop, args=(i, iterations[i]))
		processes.append(p)

	for i in n_iterations:
		processes[i].start()
		
	for i in n_iterations:
		processes[i].join()

	
	print 'Multiprocessing all DONE at:', ctime(), "elapsed time is %f seconds" % (time()-start_time)

# Now, try the same trick without multiprocessing
	n_iterations = sum(iterations)
	start_time = time()	
	print 'start a single process at:', ctime(), 'PID is ', os.getpid()
	l = 0.0
	for i in xrange(n_iterations):
            l += 1.0
	print 'done at:', ctime(), 'elapsed time is %f seconds' % (time()-start_time)
	
	

if __name__=='__main__':
	main()
