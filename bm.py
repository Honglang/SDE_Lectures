import numpy as np
import math
import matplotlib.pyplot as plt


T=1
N=1000
dt=T/float(N)
tt=np.linspace(0,1,N)

W=np.zeros(N)
W[1:N] = np.sqrt(dt)*np.random.normal(0,1,N-1)
W = np.cumsum(W)


plt.figure(1)
plt.subplot(121)
plt.plot(tt,W, linewidth=2)

plt.subplot(122)
for k in range(50):
	W=np.zeros(N)
	W[1:N] = np.sqrt(dt)*np.random.normal(0,1,N-1)
	W = np.cumsum(W)
	plt.plot(tt,W, linewidth=1)


plt.show()

