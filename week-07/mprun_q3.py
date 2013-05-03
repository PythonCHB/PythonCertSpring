#! /usr/bin/env python

# This program demonstrates that using processes does improve the execution
# time of a multiprocess program
from multiprocessing import Process, Queue
from time import time, ctime
import os

iterations = [4, 2, 7]
scaling_factor = 100000000 # Change this number so that the subprocess takes a
                            # reasonable amount of time.  CPU dependent



for i in range(len(iterations)):
    iterations[i] *= scaling_factor

def loop(nloop, iterations, q):
    start_time = time()
    print 'start loop', nloop, 'at:', ctime(), 'PID is ', os.getpid()
    l = 0.0
    for i in xrange(iterations):
        l += 1.0
# Process puts the results in the queue and then keeps going.        
    q.put( l )
    print 'loop', nloop, 'done at:', ctime(),'Elapsed time is %f seconds' % (time()-start_time) 
# process now goes to sleep until parent joins it.

def main():
    start_time = time()
    print 'starting at:', ctime(), 'PID is', os.getpid()
    processes = []
    q_list = []
    n_iterations = range(len(iterations))

    for i in n_iterations:
        q = Queue()
        q_list.append(q)
        p = Process(target=loop, args=(i, iterations[i], q))
        processes.append(p)


    for i in n_iterations:
        processes[i].start()

    all_sum = 0.0
    for i in n_iterations:
        all_sum += q_list[i].get()
        processes[i].join()
    print "Sum is %f" % all_sum
    
    print 'Multiprocessing all DONE at:', ctime(), "elapsed time is %f seconds" % (time()-start_time)

# Now, try the same trick without multiprocessing
    n_iterations = sum(iterations)
    start_time = time() 
    print 'start a single process at:', ctime(), 'PID is ', os.getpid()
    l = 0.0
    for i in xrange(n_iterations):
            l += 1.0
    print 'done at:', ctime(), 'elapsed time is %f seconds' % (time()-start_time)
    print "Sum is %f" % l
    

if __name__=='__main__':
    main()
