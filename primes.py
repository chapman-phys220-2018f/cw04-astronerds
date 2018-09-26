#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#First generate all positive integers less than n, starting from the number 2.
#Remove all multiples of 2 (greater than 2) from the generated integers.
#Remove all multiples of the next largest remaining number (greater than that number). That number will be prime by construction.
#Repeat the previous step until you remove multiples of all primes less than sqrt(n). (It turns out that stopping at $$\sqrt{n}$$ is sufficient, which saves some calculational steps.)
#Return the final set of remaining (prime) numbers less than n

#function
def eratosthenes(n):
    #using a list
    list = []
    #multiples of 2
    for i in range(2, n+1):
        if i not in list:
            print (i)
            for j in range(i*i, n+1, i):
                list.append(j)

#driver program
if __name__=='__main__': 
    n = 20
    eratosthenes(n) 