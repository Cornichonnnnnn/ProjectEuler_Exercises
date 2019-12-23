#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:44:48 2019

@author: xkong
"""
#%% P31
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
#%%
import numpy as np
# 200 = a1*100 + a2*50 + a3*20 + a4*10 + a5*5 + a6*2 + a7*1
#current_england = {'1£':0,'50p':0,'20p':0,'10p':0,'5p':0,'2p':0,'1p':0}
'''
current = np.matrix([100,50,20,10,5,2,1])
a1,a2,a3,a4,a5,a6,a7 = list(),list(),list(),list(),list(),list(),list()
num = np.matrix([a1,a2,a3,a4,a5,a6,a7])
'''
x = 0
y = 200
# 200 = current * num.T
a1,a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0,0
for a1 in range(0,int(y/100)+1,1): # a1 = [0,1,2]
    t1 = y
    t1 = t1 - a1*100
    if t1 > 0:
        for a2 in range(0,int(t1/50)+1,1): # a2 = [0:4]
            t2 = t1
            t2 = t2 - a2*50
            if t2 > 0:
                for a3 in range(0,int(t2/20)+1,1): # a3 = [0:10]
                    t3 = t2
                    t3 = t3 - a3*20
                    if t3 > 0:
                        for a4 in range(0,int(t3/10)+1,1): # a4 = [0:20]
                            t4 = t3
                            t4 = t4 - a4*10
                            if t4 > 0:
                                for a5 in range(0,int(t4/5)+1,1): # a5 = [0:40]
                                    t5 = t4
                                    t5 = t5 - a5*5
                                    if t5 > 0:
                                        for a6 in range(0,int(t5/2)+1,1): # a6 = [0:100]
                                            t6 = t5
                                            t6 = t6 - a6*2
                                            if t6 > 0:
                                                for a7 in range(0,int(t6)+1,1): # a7 = [0:200]
                                                    t7 = t6
                                                    t7 = t7 - a7*1
                                                    if t7 == 0:
                                                        print(a1,a2,a3,a4,a5,a6,a7)
                                                        x += 1
                                                        #a1,a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0,0
                                            else:
                                                a7 = 0
                                                print(a1,a2,a3,a4,a5,a6,a7)
                                                x += 1
                                                break
                                    else:
                                        a6,a7 = 0,0
                                        print(a1,a2,a3,a4,a5,a6,a7)
                                        x += 1
                                        break
                            else:
                                a5,a6,a7 = 0,0,0
                                print(a1,a2,a3,a4,a5,a6,a7)
                                x += 1
                                break
                    else:
                        a4,a5,a6,a7 = 0,0,0,0
                        print(a1,a2,a3,a4,a5,a6,a7)
                        x += 1
                        break
            else:
                a3,a4,a5,a6,a7 = 0,0,0,0,0
                print(a1,a2,a3,a4,a5,a6,a7)
                x += 1
    else:
        a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0
        print(a1,a2,a3,a4,a5,a6,a7)
        x +=1
print(x)
#%% 200 = a1*100 + a2*50 + a3*20 + a4*10
y = 200
x = 0
a1,a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0,0
for a1 in range(0,int(y/100)+1):
    t = y
    t = t - a1*100
    if t > 0:
        for a2 in range(0,int(t/50)+1,1):
            t2 = t
            t2 = t2 - a2*50
            if t2 > 0:
                for a3 in range(0,int(t2/20)+1,1):
                    t3 = t2
                    t3 = t3 - a3*20
                    if t3 > 0:
                        for a4 in range(0,int(t3/10)+1,1):
                            t4 = t3
                            t4 = t4 - a4*10
                            if t4 > 0:
                                for a5 in range(0,int(t4/5)+1,1):
                                    t5 = t4
                                    t5 = t5 - a5*5
                                    if t5 > 0:
                                        for a6 in range(0,int(t5/2)+1,1):
                                            t6 = t5
                                            t6 = t6 - a6*2
                                            if t6>0:
                                                for a7 in range(0,int(t6)+1,1):
                                                    t7 = t6
                                                    t7 = t7 - a7*1
                                                    if t7 == 0:
                                                        print(a1,a2,a3,a4,a5,a6,a7)
                                                        x += 1
                                            else:
                                                a7 = 0
                                                print(a1,a2,a3,a4,a5,a6,a7)
                                                x+=1
                                    else:
                                        a6,a7 = 0,0
                                        print(a1,a2,a3,a4,a5,a6,a7)
                                        x+=1
                            else:
                                a5,a6,a7 = 0,0,0
                                print(a1,a2,a3,a4,a5,a6,a7)
                                x+=1
                    else:
                        a4,a5,a6,a7 = 0,0,0,0
                        print(a1,a2,a3,a4,a5,a6,a7)
                        x +=1
            else:
                a3,a4,a5,a6,a7 = 0,0,0,0,0
                print(a1,a2,a3,a4,a5,a6,a7)
                x+=1
    else:
        a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0
        print(a1,a2,a3,a4,a5,a6,a7)
        x+=1
print(x)
#%%
current = np.matrix([100,50,20,10,5,2,1])































