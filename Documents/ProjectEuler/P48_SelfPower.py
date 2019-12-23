#%%
#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#%%
def selfpower(i):
    return i**i;
#%%
n = 1000;
s = 0;
for i in range(1,n+1):
    s = s + selfpower(i);
print str(s)[-10:-1],str(s)[-1]