#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:57:23 2019

@author: xkong
"""

"""
Distinct powers
Problem 29

Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    22=4, 23=8, 24=16, 25=32
    32=9, 33=27, 34=81, 35=243
    42=16, 43=64, 44=256, 45=1024
    52=25, 53=125, 54=625, 55=3125

If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

"""
#%%
disct = list()
for a in range(2,6):
    for b in range(2,6):
        if a**b not in disct:
            disct.append(a**b)
print(len(disct))
#%%
disct_10 = list()
for a in range(2,101):
    for b in range(2,101):
        if a**b not in disct_10:
            disct_10.append(a**b)
print(len(disct_10))
