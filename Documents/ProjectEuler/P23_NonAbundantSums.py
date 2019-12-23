#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:58:10 2019

@author: xkong
"""


"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""
#%%
n = 16
import numpy as np
b = list()
for i in range(int(np.sqrt(n))):
    if n%(i+1) == 0:
        b.append(i+1)
print(b)
c = b
print(c)
for index,s in enumerate(b):
    c.append(n/s)
print(c)
#%%
for s in b:
    c.append(n/s)
print(c)
