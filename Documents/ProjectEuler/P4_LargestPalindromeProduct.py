#Project 4 Largest palindrome product

#%% Origin answer
import time
start = time.clock()
for x in range(999*999,100*100,-1):
    if str(x)[0] == str(x)[-1] and str(x)[1] == str(x)[-2] and str(x)[2] == str(x)[-3]:
        for i in xrange(999,100,-1):
            if x%i == 0 and 1000> x/i > 99:
                    print '%d = %d * %d' %(x,i,x/i)
stop = time.clock()
print stop - start                  
#%% definition Inverse 
def Inverse(a):
    b = a/100 + a%10*100 + a%100/10*10
    return b
#%% 
import time
start = time.clock()    
for x in range(999,100,-1):
    for i in range(999,100,-1):
        if (x*1000 + Inverse(x))%i == 0 and (x*1000 + Inverse(x))/i<1000:
            print '%d = %d * %d' %(x*1000 + Inverse(x),(x*1000 + Inverse(x))/i,i)
stop = time.clock()
print stop - start
