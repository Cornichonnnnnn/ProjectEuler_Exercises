# P7 1001st prime

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#%%
import numpy as num
def Isprime(x):
    for i in range(2,int(num.sqrt(x))+1,1):
      if x%i == 0:
          return 1
    return 0
#%%
Prime_array=[2,3,5,7,11,13];
for i in range(15,110000,1):
    if not Isprime(i):
        Prime_array.append(i);
        print(i);
print(Prime_array[10000])