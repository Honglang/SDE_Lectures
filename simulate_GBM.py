import numpy as np
import math
import matplotlib.pyplot as plt


T=1
N=10000
dt=T/float(N)
tt=np.linspace(0,T,N)




# simulate GBM process
theta1=1
theta2=10
X0=0.5
plt.figure(2)

X=np.zeros(N)
X[0]=X0
W=np.zeros(N)
W[1:N] = np.sqrt(dt)*np.random.normal(0,1,N-1)
for i in range(N-1):
	X[i+1] = X[i] + theta1*X[i]*dt + theta2*np.sqrt(dt)*W[i+1]

plt.plot(tt,X, linewidth=2)

theta2=40
X0=0.5
plt.figure(2)

X=np.zeros(N)
X[0]=X0
W=np.zeros(N)
W[1:N] = np.sqrt(dt)*np.random.normal(0,1,N-1)
for i in range(N-1):
	X[i+1] = X[i] + theta1*X[i]*dt + theta2*X[i]*np.sqrt(dt)*W[i+1]

plt.plot(tt,X, linewidth=2)



plt.show()

