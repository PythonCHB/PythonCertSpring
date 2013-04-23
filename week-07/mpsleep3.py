#! /usr/bin/env python

from multiprocessing import Process
from time import sleep, ctime
import os

loops = [4, 2, 7]

def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', ctime(), 'PID is ', os.getpid()
	sleep(nsec)
	print 'loop', nloop, 'done at:', ctime()

def main():
	print 'starting at:', ctime(), 'PID is', os.getpid()
	processes = []
	nloops = range(len(loops))

	for i in nloops:
		p = Process(target=loop, args=(i, loops[i]))
		processes.append(p)

	for i in nloops:
		processes[i].start()
		
	for i in nloops:
		processes[i].join()

	print 'all DONE at:', ctime()

if __name__=='__main__':
	main()
