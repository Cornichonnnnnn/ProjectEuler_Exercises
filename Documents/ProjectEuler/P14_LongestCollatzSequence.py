#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#%%
def Collatz(n):
    if n%2 == 0:
        return n/2;
    else:
        return 3*n+1;
#%%
import time
start = time.clock();
limit = 1000000;
jmax = 0;
for i in xrange(1,limit):
    j = 1;
    t = i;
    while t != 1:
        t = Collatz(t);
        j = j + 1;
    if j > jmax:
        jmax = j;
        imax = i;
        print imax,jmax;
print imax,jmax
stop = time.clock()
print stop - start
#%%
def countChain(n):
    if n == 1:
        return 1;
    if n%2 == 0:
        return 1 + countChain(n/2);
    else:
        return 1 + countChain(3*n+1)
        
#%%%
import time
start = time.clock();
limit = 1000000;
jmax = 0;
for i in xrange(1,limit):
    if countChain(i) > jmax:
        jmax = countChain(i);
        imax = i;
        print imax,jmax;
print imax,jmax 
stop = time.clock()
print stop - start
#%%
a = 4
b = 5
print('%i + %i = %s' %(a,b,a+b))
