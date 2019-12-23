#  Project-1
#  If we list all the natural number below 10 that are multiples of 3 or 5,
#  we get 3,5,6 and 9. The sum of these multiples is 23.
#  -------------------------------------------------------------------------
#  Q: Find the sum of all the multiples of 3 or 5 below 1000
#%%
import numpy as np
import timeit
#from matplotlib import pyplot as plt
setup_1 = '''
target = 999
sum_temp = 0
for i in range(0,target+1):
    if i%5 == 0 or i%3 == 0:
        sum_temp = sum_temp + i
print(sum_temp)
'''
timeit.timeit(setup=setup_1)
#%% Functional method
setup_2 = '''
target = 999
def SumDivisibleBy(n):
    p = target/n
    return n*p*(p+1)/2
a = SumDivisibleBy(3);
b = SumDivisibleBy(5);
c = SumDivisibleBy(15);
print(a+b-c)
'''
timeit.timeit(setup=setup_2)
#%% Simplified answer in one line
import timeit
setup_3 = '''
target = 999
sum([i for i in range(target+1) if i%3==0 or i%5==0])
'''
timeit.timeit(setup=setup_3)
#%%
#timeit.timeit("sum([i for i in range(999+1) if i%3==0 or i%5==0])")
t = timeit.Timer("sum([i for i in range(1000) if i%3==0 or i%5==0])")
t.timeit(1)
#print(sum([i for i in range(target+1) if i%3==0 or i%5==0]))