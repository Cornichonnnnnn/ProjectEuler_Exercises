import numpy as np
from matplotlib import pyplot as plt
#%%
def isotropic_nonlinear(x, *p):
    E, Rp, Rm, A = p
    return(np.piecewise(x, [x<Rp/E, x>=Rp/E], [lambda x: E*x, lambda x: Rp + (Rm-Rp)*(1-np.exp(-A*(x-Rp/E)))]))
    
#%%
modulus = 70e3;
sigy = 400;
sigm = 450;
epsilon = range(0,1,0.01);
plt.plot(epsilon,isotropic_nonlinear(epsilon,*[modulus,sigy,sigm,10]))