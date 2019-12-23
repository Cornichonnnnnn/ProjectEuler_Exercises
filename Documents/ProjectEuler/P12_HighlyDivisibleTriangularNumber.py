import numpy as np
#%%
def TriangularNumber(n):
    return (n*(n+1)/2);
#%%
def HowManyDivisors(n):
    j = 0;
    if n > 1:
        for i in range(1,int(np.sqrt(n)+1)):
            if n%i == 0:
                j = j + 2;
        if int(np.sqrt(n)) == np.sqrt(n):
            return j-1
        else:
            return j
    else:
        return 1;
#%%
limit = 900000000;
for i in xrange(1,limit):
    if HowManyDivisors(TriangularNumber(i)) > 500:
        print i;
#%%
i = 1;
while HowManyDivisors(TriangularNumber(i)) < 500:
    i = i + 1;
    print i,TriangularNumber(i)
print i, TriangularNumber(i), HowManyDivisors(TriangularNumber(i));