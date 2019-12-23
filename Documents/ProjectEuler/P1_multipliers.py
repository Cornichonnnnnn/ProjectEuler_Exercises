#  Project-1
#  If we list all the natural number below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23. 
#  Q: Find the sum of all the multiples of 3 or 5 below 1000
#%%
import numpy as np
#from matplotlib import pyplot as plt 
#%%
target = 999;
sum_temp = 0;
#%%
for i in xrange(0,target+1):
    if i%5 == 0 or i%3 == 0:
        sum_temp = sum_temp + i
print(sum_temp)

#%% Functional method
def SumDivisibleBy(n):
    p = target/n
    return n*p*(p+1)/2
#%%
a = SumDivisibleBy(3);
b = SumDivisibleBy(5);
c = SumDivisibleBy(15);
print(a+b-c)

#%% Simple answer
print(sum([i for i in range(target+1) if i%3==0 or i%5==0]))