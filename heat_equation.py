

import scipy as sp
import numpy as np
import time
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from pylab import *

dx=0.01
dy=0.01
a=0.5
timesteps = 500

nx=int(1/dx)
ny=int(1/dy)

dx2 = dx**2
dy2 = dy**2

dt = dx2*dy2/( 2*a*(dx2+dy2) )

u=np.zeros([nx,ny,timesteps])


for i in range(nx):
   for j in range(ny):
      if ( ( (i*dx-0.5)**2+(j*dy-0.5)**2 <= 0.1) & ((i*dx-0.5)**2+(j*dy-0.5)**2>=.05) ):
            u[i,j,0] = 1



for t in range(timesteps-1):
	u[1:-1, 1:-1,t+1] = u[1:-1, 1:-1,t] + a*dt*( (u[2:, 1:-1,t] - 2*u[1:-1, 1:-1,t] + u[:-2, 1:-1,t])/dx2 + (u[1:-1, 2:,t] - 2*u[1:-1, 1:-1,t] + u[1:-1, :-2,t])/dy2 )



fig = plt.figure(1)
plt.subplot(141)
plt.contourf(u[:,:,0], cmap=plt.cm.winter)


plt.subplot(142)
plt.contourf(u[:,:,100], cmap=plt.cm.winter)
plt.subplot(143)
plt.contourf(u[:,:,250], cmap=plt.cm.winter)
plt.subplot(144)
plt.contourf(u[:,:,400], cmap=plt.cm.winter)

plt.show()



