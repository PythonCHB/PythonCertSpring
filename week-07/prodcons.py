#!/usr/bin/env python

from random import randint
from time import sleep
from Queue import Queue
from mythread import My_thread
QUEUE_SIZE = 6

def writeQ(queue):
    print 'Producing object for Q...',
    if queue.full() :
        print "queue is full, writeQ will block"
        block = True
    else :
        block = False
    queue.put('xxx', block=1)
    if block :
        print "writeQ is now unblocked"
    print 'size now', queue.qsize()
    
def readQ(queue):
    if queue.empty() :
        print "readQ will block"
        block = True
    else :
        block = False
    val = queue.get(block=1)
    if block :
        print "readQ is now unblocked"
    print 'consumed object from Q... size now', queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(8, 20)
    q = Queue(QUEUE_SIZE)

    threads = []
    for i in nfuncs:
        t = My_thread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'all DONE'

if __name__ == '__main__':
    main()

