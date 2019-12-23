#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:26:47 2019

@author: xkong
"""


"""
Names scores
Problem 22
----------
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
#%%
dir = '/home/xkong/Documents/ProjectEuler/data/'
file_name = 'P22_NamesScore.txt'
f = open(dir+file_name,'r')
#for index,s in enumerate(f):
contents = f.read()
cut = contents.strip().split(',')
cut.sort()
print(cut)
f.close()
score = list()
total = 0
for index,s in enumerate(cut):
    name = 0
    for i in cut[index][1:-1]:
        name += ord(i) - 64
    print(index+1,s,name,(index+1)*name)
    total += (index+1)*name
print(total)
#%%
s = 0
a = '"COLIN"'
for i in a[1:-1]:
    s += ord(i)-64
print(s)
#%%
"""
help(ord)

ord(c, /)
    Return the Unicode code point for a one-character string.
"""