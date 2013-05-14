#!python

import multiprocessing
from time import sleep, ctime

loops = [4, 2, 7]

class My_thread ( threading.Thread ):
    def __init__(self, func, args, name=''):
# This is the way the documentation says to do it
#                threading.Thread.__init__(self)   # intialize the superclass
# This is the way we did it in week 6
        threading.super().__init__(self)
        self.name = name
        self.func = func
        self.args = args
    
    def run(self):
        self.func ( *self.args )    

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = My_thread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__=='__main__':
    main()
