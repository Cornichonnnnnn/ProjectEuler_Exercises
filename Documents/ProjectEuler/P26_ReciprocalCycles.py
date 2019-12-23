#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:13:14 2019

@author: xkong
"""
#%%
'''
Reciprocal cycles

Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
#%%
import numpy as np

for i in range(1,100):
    a = str(np.float128(1/i))
    #print(i)
    if len(a) >= 22:
        b = a[0:-4]
        for j in range(9,1,-1):
            for k in range(2,9):
                if b[k:2+j] == b[k+j:k+j+j]:
                    print(b,i,j,k)
                    break
#%%
for i in range(2,12):
    res = '0.'
    num = list()
    a = 1
    j = 1
    while j<20:
        while a < i:
            a  = a * 10
            if a == 0:
                break
            #res+='0'
        b  = a // i # 10//11 = 0;
        a  = a % i # res 10%11 = 10;

        if str(b) in res and b > 0:
            for index,k in enumerate(res):
                if k == str(b):
                    same = res[index:]
                    break
            break
        res += str(b)

        if a == 0: #and b == 0: # case 1° j < 10:      2°10 < j < 100
            same = ''
            break
        #res += str(b)
        j += 1
    print(i,res[:],same,len(same),1/i)
#%%
'''
a b
a = 0, b !=0 ->

i.e 1/3; a = 10, b = a//3 = 3, a = 10%3 = 1;
 1/2 ; a = 10, b = a//2 = 5, a = 10%2 = 0;
 1/11 ; a = 10, b = a//11 = 0, a = 10%11 = 11

'''
#%%
ii = 100
res_ = '0.012301230'
for index,i in enumerate(res_):
    print(res_[index:index+len(str(ii))])
#%%
for i in range(1,500):
    j = 1
    k = i
    while k//10 > 0:
        k = k//10
        j=j+1
    print(i,j)
    print(i,len(str(i)))

    #%%
def distance(x0,y0,x1,y1):
    import numpy as np
    return np.sqrt((x1-x0)**2+(y1-y0)**2)

