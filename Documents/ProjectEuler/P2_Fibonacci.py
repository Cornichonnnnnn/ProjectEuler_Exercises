# Problem 2: Fibonacci sequence
# Find the sum of all the even-valued terms which do not exceed 4000000
import numpy as num
#%% My answer
limit = 4000000;
Fnum = [];
Fnum.append(1);
Fnum.append(2);
Sum_Fnum = 2;
i = 1;
while Fnum[i] + Fnum[i-1] < limit:
    Fnum.append(Fnum[i] + Fnum[i-1]);
    i+=1;
    if Fnum[i] %2 == 0:
        Sum_Fnum = Sum_Fnum + Fnum[i];
print(Sum_Fnum)
#%% Silplified answer 
limit = 4000000;
Sum_Fnum = 0;
a = 1;
b = 1;
c = a + b;
while c < limit:
    Sum_Fnum += c;
    a = b + c;
    b = c + a;
    c = a + b;
    print(c);
print(Sum_Fnum)
#%% More simplified: 
# F(n) = 4*F(n-3) + F(n-6) 
# E(n) = 4*E(n-1) + E(n-2)
limit = 4000000;
Sum_Fnum = 0;
a = 2;
b = 8;
c = 4*b + a;

while c < limit:
    Sum_Fnum += c;
    a = b;
    b = c;
    c = 4*b + a;
    print(c);
print(Sum_Fnum)