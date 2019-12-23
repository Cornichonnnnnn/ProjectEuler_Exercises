#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:41:04 2019

@author: xkong
"""

#%%
'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

#%%
def DividNumber(i):
    hundred,tens,ones = int(i/100), int((i/10)%10) , i%10
    return hundred,tens,ones
#%%
hundred,tens,ones = DividNumber(5)
print(hundred,tens,ones)
#%%
Letter_Ones = ['zero','one','two','three','four','five','six','seven','eight','nine']
Number_Ones = [len(i) for i in Letter_Ones]
Letter_Ten = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
Number_Ten = [len(i) for i in Letter_Ten]
Letter_Tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
Number_Tens = [len(i) for i in Letter_Tens]
Letter_Thousand = 'thousand'
Number_Thousand = len(Letter_Thousand)
#%%
def NumLetterCounts(i):
    count = 0
    read = ''
    thousand, hundred, tens, ones = int(i/1000),int((i/100)%10), int((i/10)%10) , i%10
    if thousand:
        count += Number_Ones[thousand] + len('thousand')
        read += Letter_Ones[thousand] + ' thousand '
    if hundred:
        if tens or ones:
            count += Number_Ones[hundred] + len('hundred') + len('and')
            read += Letter_Ones[hundred] + ' hundred' + ' ' + 'and'
        else:
            count += Number_Ones[hundred] + len('hundred')
            read += Letter_Ones[hundred] + ' hundred'
    if tens == 1:
        count += Number_Ten[ones]
        read += Letter_Ten[ones]
    elif tens != 0:
        count += Number_Tens[tens-2]
        read += ' ' + Letter_Tens[tens-2]
        if ones:
            count += Number_Ones[ones]
            read += '-' + Letter_Ones[ones]
    elif ones:
        count += Number_Ones[ones]
        read += ' ' + Letter_Ones[ones]
    return count,read
#%%
count_total = 0
for i in range(1,1001):
    a,b = NumLetterCounts(i)
    count_total += a
    print(b,a,count_total)

