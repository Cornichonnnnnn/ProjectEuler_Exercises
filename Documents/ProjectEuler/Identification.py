#comportements et techniques d'identification
#%% R = R0 + Q(1-exp(-bp))
def isotropic_hardening (x,*p):
    R0,Q,b = p;
    return R0 + Q*(1-exp(-b*x));
#%%
from matplotlib import pyplot as plt
    x = [1,2,3,4,5];
    plt.plot(x,x^2)
#%% Hardening 
sig = R0 + Q * (1 - exp(-b*p) )   # isotropic nonlinear
         + H * p                  # kinematic linear
         + C/D *(1 - exp(-D*p))   # kinematic nonlinear
         + n*(pdot)^(1/n)         # viscous norton flow 
     