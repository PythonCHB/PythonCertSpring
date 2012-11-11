#! /usr/bin/env python
#
# A program to compare the speed of a list and an integer by searching for a
# random number

import random
import time

def populate ( size, num_range ) :
    "This subroutine populates a_list and a_dict with random numbers"

    a_dict={}
    a_list=[]
    for i in range(size) :
        v = random.randint(0, num_range) # Return a random integer N such that a <= N <= b.
        a_dict[v] = 1
        a_list.append(v)
    return (a_dict, a_list)
        

size=int(raw_input("Enter how big you want the list and the dictionary to be "))
num_range=int(raw_input("Enter the range of random numbers "))
iterations=int(raw_input("Enter the number of iterations to loop over "))

a_dict, a_list = populate(size, num_range)

start_time = time.time()
for i in range(iterations) :
    in_list = random.randint(0, num_range) in a_list
end_time = time.time()
print "It took ", end_time - start_time, "seconds to find the random number in the list"
start_time = time.time()
for i in range(iterations) :
    in_list = random.randint(0, num_range) in a_dict
end_time = time.time()
print "It took ", end_time - start_time, "seconds to find the random number in the dictionary"

