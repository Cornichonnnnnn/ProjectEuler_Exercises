#Summation of primes
# Problem 10 : 
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#%%
import numpy as num
def Isprime(x):
    for i in range(2,int(num.sqrt(x))+1,1): 
      if x%i == 0:
          return 1
    return 0
#%%
target = 2000000;
Prime_array=[2,3,5,7,11,13];
S = 2+3+5+7+11+13;
for i in range(15,target,1):
    if not Isprime(i):
        S = S + i;
print S