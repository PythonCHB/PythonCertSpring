#!/usr/bin/env python

from random import randint
from time import sleep
from Queue import Queue
from mythread import My_thread
from threading import RLock


QUEUE_SIZE = 6

def writeQ(queue):
    mutex_print ( 'Producing object for Q...' )
    if queue.full() :
        mutex_print ( "queue is full, writeQ will block" )
        block = True
    else :
        block = False
    queue.put('xxx', block=1)
    if block :
        mutex_print ( "writeQ is now unblocked" )
    mutex_print ( 'size now %d'% queue.qsize() )
    
def readQ(queue):
    if queue.empty() :
        mutex_print ( "readQ will block" )
        block = True
    else :
        block = False
    val = queue.get(block=1)
    if block :
        mutex_print ( "readQ is now unblocked" )
    mutex_print ('consumed object from Q... size now %d' % queue.qsize() )

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

def mutex_print( string ):
    print_lock.acquire()
    print string
    print_lock.release()
    

funcs = [writer, reader]
nfuncs = range(len(funcs))
print_lock = RLock()

def main():
    nloops = 20
    q = Queue(6)

    threads = []
    for i in nfuncs:
        t = My_thread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

# no need to invoke mutex_print here because all of the threads are terminated
    print 'all DONE'

if __name__ == '__main__':
    main()

