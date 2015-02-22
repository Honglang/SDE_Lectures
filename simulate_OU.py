import numpy as np
import math
import matplotlib.pyplot as plt


T=10
N=10000
dt=T/float(N)
tt=np.linspace(0,T,N)


# simulate OU process
theta1=1
theta2=2
theta3=1
X0=0.5
ax = plt.figure(1)

X=np.zeros(N)
X[0]=X0
W=np.zeros(N)
W[1:N] = np.sqrt(dt)*np.random.normal(0,1,N-1)
for i in range(N-1):
	X[i+1] = X[i] + (theta1 - theta2*X[i])*dt + theta3*np.sqrt(dt)*W[i+1]

ax=plt.subplot(111)
plt.plot(tt,X, linewidth=2)
ax.set_ylim([0.45,0.55])
plt.show()




