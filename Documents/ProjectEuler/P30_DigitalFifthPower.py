#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:15:37 2019

@author: xkong
"""

#%%
'''
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
#%%
a = [i**5 for i in range(0,10)]
print(a)
#%% 4 digital number
s4 = 0
n = 5
for i1 in range(1,10):
    for i2 in range(0,10):
        for i3 in range(0,10):
            for i4 in range(0,10):
                s1 = i1*1000 + i2*100 + i3*10 + i4
                s2 = i1**n + i2**n + i3**n + i4**n
                if s1 == s2:
                    print(s1)
                    s4 += s1
print(s4)
#%% only 5 digital num
s0 = 0
for i1 in range(0,10):
    for i2 in range(0,10):
        for i3 in range(0,10):
            for i4 in range(0,10):
                for i5 in range(0,10):
                    s1 = i1*10000 + i2*1000 + i3*100 + i4*10 + i5
                    s2 = i1**5 + i2**5 + i3**5 + i4**5 + i5**5
                    if s1 == s2:
                        print(s1)
                        s0 += s1
print(s0)
#%%
import time
#%% 6 digital num
start = time.time()
s0 = 0
for i1 in range(0,10):
    for i2 in range(0,10):
        for i3 in range(0,10):
            for i4 in range(0,10):
                for i5 in range(0,10):
                    for i6 in range(0,10):
                        s1 = i1*100000 + i2*10000 + i3*1000 + i4*100 + i5*10 + i6
                        s2 = i1**5 + i2**5 + i3**5 + i4**5 + i5**5 + i6**5
                        if s1 == s2:
                            print(s1)
                            s0 += s1
end = time.time()
print(s0, end-start)

#%%
def Sum_Fifth_power(n):
    sum_ = 0
    for i in str(n):
        sum_ += int(i)**5
    return sum_
#%%
import time
start = time.time()
S0 = 0
for i in range(0,200000):
    if Sum_Fifth_power(i) == i:
        print(i)
        S0 += i
end = time.time()
print(S0,end-start)

