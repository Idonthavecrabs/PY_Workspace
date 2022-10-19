# -*- coding: utf-8 -*-

"""
Created on Mon Oct  3 13:59:21 2022

@author: RUBIN

Code to compare n! with its approximation sqrt(2*pi*n)*(n/e)^n
"""

import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
e  = np.e
MAX = 150 #Highest value of x in x! used for comparison
# =============================================================================
# Create Factorial Arra
# =============================================================================
def Fact(x):
    fac=[]
    Prod = 1
    for i in range(x):
        if i==0:
            fac.append(1)
        else:
            Prod = Prod * i
            fac.append(Prod)
    return fac

# =============================================================================
# Create Plots
# =============================================================================

#Fig 1
x = np.arange(0,MAX,1)
test = Fact(max(x))
Factorial = Fact(max(x))
Approx = ((2*pi*x)**0.5)*(x/e)**x
plt.yscale("log")

plt.plot(x[:-1],Factorial)
plt.plot(x,Approx)
# plt.plot(x,((2*pi*x)**0.5))

plt.show()

#Fig 2 - Error between Factorial and approximation plots
plt.figure(num=2)
plt.yscale("log")
#Remove 'zero' point and equalize array/list sizes
plt.plot(x[1:-1],(Factorial[1:]-Approx[1:-1])/Factorial[1:]*100)
plt.show()