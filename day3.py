'''
This program works will in Ipython
Learn from BarbaGroup
Author Leo
'''

# Assigning module
import numpy as np
import matplotlib.pyplot as plt
import time, sys

# Variable Decalaration
nx = 41
dx = 2. / (nx - 1)
nt = 25
nu = 0.3  # the value of viscosity
c  = 1
sigma = 0.2    # cfl (courant number)
dt = sigma * dx ** 2 / nu / c

# Assigning Initial Field
u = np.ones(nx)
u[int(0.5 / dx):int(1 / dx + 1)] = 2

# initialize figure
plt.figure(figsize=(10,10), dpi=100)
plt.plot(np.linspace(0, 2, nx), u)

# calculation begin
un = np.ones(nx)    # temp array
for n in range(nt): #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 *(un[i+1] - 2*un[i] +  un[i - 1])

plt.plot(np.linspace(0, 2, nx), u)
plt.show()
