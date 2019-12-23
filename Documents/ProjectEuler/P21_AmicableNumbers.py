#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:52:47 2019

@author: xkong
"""

'''
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
#%%
import numpy as np
def NumDivisor(n):
    num = 0
    num_list = list()
    num_list.append(1)
    a = int(np.sqrt(n))
    for i in range(2,a+1):
        if n%i == 0:
            num += 1
            num_list.append(i)
    if int(np.sqrt(n)) == np.sqrt(n):
        for i in range(len(num_list)-2,0,-1):
            num_list.append(int(n/num_list[i]))
        return num_list
    else:
        for i in range(len(num_list)-1,0,-1):
            num_list.append(int(n/num_list[i]))
        return num_list
#%%
import time
start = time.time()
sum_all = 0
for i in range(1,10000+1):
    j = sum(NumDivisor(i))
    k = sum(NumDivisor(j))
    if i == k and i !=j and i<j:
        print(i,j,k)
        sum_all = sum_all + i + j
end = time.time()
print(sum_all)
print(end-start)
#%% Corrigé
import time
start = time.time()
sum_all = 0
for i in range(1,10000+1):
    j = sum(NumDivisor(i))
    if i<j:
        k = sum(NumDivisor(j))
        if i == k :
            print(i,j,k)
            sum_all = sum_all + i + j
end = time.time()
print(sum_all)
print(end-start)












