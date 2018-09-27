#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Alley Busick
# Student ID: 2293544
# Email: busick@chapman.edu
# Course: PYHS220/MATH220/CPSC220 Fall 2018
# Assignment: CW 4
###

import math

#function
def eratosthenes(n):

    sieve = [True] * n
    #zero and one are not prime
    sieve[0] = False
    sieve[1] = False

    #algorithm
    #marker/prime by construction
    for i in range(2, int(math.sqrt(n)) + 1):
        marker = i * 2
        while marker < n:
            sieve[marker] = False
            marker += i

    #list of primes
    primelist = []
    for i in range(n):
        if sieve[i] == True:
            #sieve list appends to new prime list if i is true
            primelist.append(i)

    return primelist

def gen_eratosthenes():
    prime_list = list(range(2, 10000))
    prime_list = [i for i in prime_list if ((i % 2 != 0) or (i == 2))]
    x = -1
    n = 0
    while True:
        x = x + 1
        n = prime_list[x]
        yield n
        for a in prime_list:
            if (a != n and a % n == 0):
                prime_list.remove(a)

#program
def main(argv):
    n = int(argv[1])
    print(eratosthenes(n))

#protects code
if __name__ == "__main__":
    import sys
    main(sys.argv)
