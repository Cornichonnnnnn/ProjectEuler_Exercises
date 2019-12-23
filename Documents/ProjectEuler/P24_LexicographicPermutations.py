#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:09:42 2019

@author: xkong
"""

"""
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
#%%
def f(n):
    import math
    return math.factorial(n)
#%%
#%%
n = 10
a = [i for i in range(n)]
b = ''
grand = 2000000
ref = grand - 1
for i in range(n-1,-1,-1):
    print(i,':',ref,"=",f(i),"*",int(ref/f(i)),"+",ref - int(ref/f(i))*f(i))
    b = b + str(a.pop(int(ref/f(i))))
    print('Here b:',b)
    ref = ref % f(i)
    #ref = ref - int(ref/f(i))*f(i) #= ref = ref % f(i)
print(b)
#%% Simplified version
import time
start = time.time()
n = 10
ipt = [i for i in range(n)]
opt = ''
order = 1000000
ref = order - 1
for i in range(n-1,-1,-1):
    #print(i,':',ref,"=",f(i),"*",ref//f(i),"+",ref % f(i))
    opt = opt + str(ipt.pop(ref//f(i)))
    ref = ref % f(i)
print(opt)
end = time.time()
print(end-start)
#%% Other expensive way
import time
start = time.time()
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
listarray=sorted(list(all_perms(('0123456789'))))
print(listarray[999999])
end = time.time()
print(end-start)