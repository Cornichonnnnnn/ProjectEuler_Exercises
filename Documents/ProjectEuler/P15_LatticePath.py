"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
#%%
def sort_C(a,b):
    x = 1
    if a > b:
        return x
    else:
        for i in range(0,a):
            x = x*(b-i)/(i+1)
    return x
#%%
y = 1
for i in range(1,20):
    y += sort_C(i,i+19)
    print(y,i)
print(y*2)
#%%
print(2*(sort_C(1,20)+sort_C(2,21)+...+sort_C(19,38)))
print(2*(1+sort_C(1,4)+sort_C(2,5)+sort_C(3,6)))#4*4
print(2*(1+sort_C(1,3)+sort_C(2,4))) #3*3
print(2*(1+sort_C(1,2))) #2*2