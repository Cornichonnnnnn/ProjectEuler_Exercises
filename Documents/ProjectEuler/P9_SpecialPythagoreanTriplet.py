#P9 a + b + c = 1000, a² + b² = c²
# c < 500, c = 1000 - a - b < a + b
#%%
s = 1000;
for c in range(s/2-1,s/3,-1):
    for b in range(c-1,s/4,-1):
        if c*c-b*b == (s-b-c)*(s-b-c):
            a = s - b - c;
            print a,b,c,a*b*c;