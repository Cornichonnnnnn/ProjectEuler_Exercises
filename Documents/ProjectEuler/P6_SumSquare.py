#Sum square difference
SqSum = 0;
begin = 1;
target = 100;
for i in range(begin,target+1,1):
    SqSum = SqSum + i*i

Sum = (1+target)*target/2;
Diff = Sum*Sum - SqSum;
print '%d - %d = %d' %(Sum*Sum,SqSum,Diff)

#%%
Sum = (1+target)*target/2;
SqSum = (2*target+1)*(target+1)