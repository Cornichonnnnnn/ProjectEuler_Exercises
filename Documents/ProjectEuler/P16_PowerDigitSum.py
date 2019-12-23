#%% P16 Power Digit Sum
#
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
a = str(2**1000);
s = 0;
for i in range(0,len(a)):
    s = s + int(a[i]);
print(s)
#%%
sum([int(i) for i in str(2**1000)])
#%%
sum(map(int,str(2**1000)))

#%% Map: map(function,sequence)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))