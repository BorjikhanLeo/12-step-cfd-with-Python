from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import pyplot, cm

nx = 81
ny = 81
nt = 100
c  = 1
dx = 2. / (nx - 1)
dy = 2. / (ny - 1)

sigma = 0.2
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((nx, ny))
un = numpy.ones((nx, ny))

u[int(.5 / dx):int(1. / dx + 1), int(0.5 / dy): int(1.0 / dy + 1)] = 2
  
fig = pyplot.figure(figsize=(10,10), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x,y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
  
u = numpy.ones((nx , ny))
u[int(.5 / dx):int(1. / dx + 1), int(0.5 / dy): int(1.0 / dy + 1)] = 2

for n in range(nt + 1):
    un = u.copy()
    row, col = u.shape
    for i in range(1, row):
        for j in range(1, col):
            u[i,j] = (un[i,j] - (c * dt / dx *(un[i,j] - un[i,j-1])) - \
             (c * dt / dy * (un[i,j] - u[i-1,j])))
            
            u[0,:] = 1
            u[-1,:] = 1
            u[:,0] = 1
            u[:,-1] = 1
             
fig = pyplot.figure(figsize=(10,10), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)


















