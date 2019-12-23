#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:18:25 2019

@author: xkong
"""
"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
#%%
ini = (365%7 + 1)%7
a = [31,28,31,30,31,30,31,31,30,31,30,31] # days
a_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
b = [i%7 for i in a]
b_leap = [i%7 for i in a_leap]
y = 1901
count = 0
#%%
for i in range(1901,2001):
    if i%4 == 0:
        c = b_leap
        print(f'{i} is a leap year')
    else:
        c = b
        print(f'{i} is not a leap year')
    for j in range(0,12):
        ini = (ini + c[j])%7
        print(ini)
        if not ini:
            count += 1
            print(f'first day of month no.{j+2}, year {i} is {count}th Sunday')