#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:13:06 2019

@author: xkong
"""

#%%
import numpy as np
import random
n = 10  # map size
m = 20  # mine num
ans_map_1 = np.zeros(n*n)
#print(ans_map_1)
mine_pos = range(n*n)
for i in random.sample(mine_pos,m):
    ans_map_1[i] = 99  # means mine
#print(ans_map_1)
ans_map = ans_map_1.reshape(n,n)
#print(ans_map)
#Generate
for i in range(n):
    for j in range(n):
        #print('I am here:',i,j)
        if ans_map[i][j] == 0:
            for k in range(max(i-1,0),min(i+1,n-1)+1):
                for l in range(max(j-1,0),min(j+1,n-1)+1):
                    if ans_map[k][l] == 99:
                        ans_map[i][j] += 1
#print(ans_map)
#%%
#n = 10
show_map = np.ones([n,n])
for i in range(n):
    for j in range(n):
        show_map[i,j] = -1
print(show_map)
#%%
#%%
def dig_mine(r1,c1):
    n = 10
    if ans_map[r1][c1] == 99:
        print('Bomb!You lost!!!')
        print(ans_map)
    else:
        for k in range(max(r1-1,0),min(r1+1,n-1)+1):
            for l in range(max(c1-1,0),min(c1+1,n-1)+1):
                if ans_map[k][l] != 99:
                   show_map[k][l] = ans_map[k][l]
        print(show_map)
#%%
dig_mine(4,0)
#%%
