#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 01:14:11 2019

@author: xkong
"""
'''
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
#%%
import numpy as num
def Isprime(x):
    for i in range(2,int(num.sqrt(x))+1):
      if x%i == 0:
          return 1
    return 0
#%%
Prime_array=[2,3,5,7,11,13];
for i in range(15,1000000,1):
    if not Isprime(i):
        Prime_array.append(i);
        print(i);
#print(Prime_array[10000])
#%%
for i in range(-1,len(Prime_array)-1,-1):
    for j in range(i-1,len(Prime_array)-1,-1):
        if i - j in Prime_array:
            print(i)
        else:
            k = i - j
            while k > 0:
                k = k -
