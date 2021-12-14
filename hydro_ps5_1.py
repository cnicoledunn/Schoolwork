#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import scipy as sp
import scipy.optimize

def concentration(t: float, D: float, radius: int) -> float:
    """Returns the concentration of a point source contaminant"""
    time = 86400*t
    sigma = np.sqrt(2*time*D)
    pie = (2*3.14159265)**(3/2)
    temp = (1/(pie*(sigma**3)))*(1e6)
    exponential = np.exp((-3/2)*((radius/sigma)**2))
    return temp*exponential

D = 9.8e-6 #Diffusion coefficient
r = np.linspace(0, 101, 101, True) #An array of all integers in the range 0 - 100
t = 30 #Days elapsed since contaminant first deposited

plt.scatter(r, concentration(t, D, r), c ="mediumaquamarine")
plt.xlabel("Radius (cm)")
plt.ylabel("Concentration (mg/L)")
plt.title("Concentration v.s. Radial Distance at T = 30 Days (Water)")
plt.show()

#Determines the number of days elapsed necessary to achieve a particular concentration at x=0cm
mintime = sp.optimize.root(lambda t: concentration(t, D, 0) - 0.005, 200)
#Extracts the x attribute from the above OptimizeSolution object
temp = mintime.x
print (temp[0])