#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:41:41 2019

@author: xkong
"""

#%%
'''
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''
#%%
def multiply(n):
    sum = 1
    for i in range(1,n):
        sum *= i
    return sum
#%%
a = str(multiply(100))
b = 0
for i in a:
    b += int(i)
print(b)