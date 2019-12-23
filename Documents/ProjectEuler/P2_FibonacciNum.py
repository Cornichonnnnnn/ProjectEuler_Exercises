import numpy as num
#%% Fibonacci number array
def Fibo(n):
    if(n<=0):
        return 0
    Fibo_array = num.zeros(n+1)
    Fibo_array[1] = 1;
    for i in range(2,n+1):
        Fibo_array[i] = Fibo_array[i-1] + Fibo_array[i-2]
    return Fibo_array[n]
#%% Function for nth Fibonacci number 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
#%%Fibonacci number sum array
def Sum_Fibo(n):
    if(n<=0):
        return 0
    Fibo_array = num.zeros(n+1)
    Fibo_array[1] = 1;
    Sum = Fibo_array[0]+Fibo_array[1];
    for i in range(2,n+1):
        Fibo_array[i] = Fibo_array[i-1] + Fibo_array[i-2]
        Sum += Fibo_array[i];
    return Sum