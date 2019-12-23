#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:55:34 2019

@author: xkong
"""

"""
1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
#%%
import numpy as np
def Fibo(n):
    if(n<=0):
        return 0
    Fibo_array = np.zeros(n+1)
    Fibo_array[1] = 1;
    for i in range(2,n+1):
        Fibo_array[i] = Fibo_array[i-1] + Fibo_array[i-2]
    return Fibo_array[n]
#%%
import time
start = time.time()
i_1 = 1 # 1st Fibonacci Num
i_2 = 1 # 2nd Fibonacci Num
n = 2
a = i_1 + i_2 # 3rd Fibonacci Number
m = 999 # (m+1) digital num
while a < 10**m:
#while len(str(a)) < m:
    a = i_1 + i_2
    i_1 = i_2
    i_2 = a
    n+=1
print(n,a)
end = time.time()
print(end-start) # 17ms
#%%
import time
start = time.time()
fibo = [1, 1]

while(True):
    fibo.append(fibo[-2] + fibo[-1])
    if len(str(fibo[-1])) > pow(10, 3) - 1:
        break

print(len(fibo))
end = time.time()
print(end-start)
