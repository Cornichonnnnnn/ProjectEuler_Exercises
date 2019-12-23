#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:51:37 2019

@author: xkong
"""

def calcul_24(A):
    return A+A

#%%
def cal(a,b,i):
    if i == '+':
        c = a + b
    if i == 1:
        c = a - b
    if i == 2:
        c = a * b
    if i == 3:
        c = a / b
    return c
#%%
def math_symbol(i):
    if i == 0:
        return '+'
    if i == 1:
        return '-'
    if i == 2:
        return '*'
    if i == 3:
        return '/'
    else:
        return 'Error: no invalid input num'
#%%
A = [5,3,4,2]
for i in range(4):
    a1 = cal(A[0],A[1],i)
    for j in range(4):
        a2 = cal(a1,A[2],j)
        for k in range(4):
            a3 = cal(a2,A[3],k)
            if a3 == 24:
                print(A[0],math_symbol(i),A[1],math_symbol(j),A[2],math_symbol(k),A[3],'=',a3)


#%% Order + - and * / (priority)
# if i j k == (0,1) or == (2,3)  -> no order
# if i j k == (0,1,2,3)          -> (2,3) priority, then (0,1)

#%%
# A = [a,b,c,d]
# if i -> a,b = A.pop(0),A = pop(0), ab = cal(a,b,i), A.append(ab)
# if j -> b,c = A.pop(1),A = pop(1), bc = cal(b,c,j), A.append(ab)
# if k -> b,c = A.pop(2),A = pop(2), cd = cal(c,d,k), A.append(ab)
#%%
a = [2,3,4,5]
b = []
#%%
for i in range(len(a)):

    b.append(a.pop(i))
    #print(a,b)
    for j in range(len(a)):
        b.append(a.pop(j))
        #print(a,b)
        for k in range(len(a)):
            b.append(a.pop(k))
            b.append(a.pop())
            print(a,b)
            a = [2,3,4,5]
            b = []
















