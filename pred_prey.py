
import numpy as np
import math
import matplotlib.pyplot as plt


a10=1.0
a12=0.02
a21=0.01
a20=1.0

T = 20.0
N = 2000
dt = T / float(N)
tt=np.linspace(0,T,N)

XX=np.zeros(N)
YY=np.zeros(N)
XX1=np.zeros(N)
YY1=np.zeros(N)

XX[0] = 120.0
YY[0] = 40.0
XX1[0] = 120.0
YY1[0] = 40.0


for i in range(N-1):
	N1=np.sqrt(dt)*np.random.normal(0,1)
	N2=np.sqrt(dt)*np.random.normal(0,1)
	XX[i+1] = XX[i] + dt*XX[i]*(a10-a12*YY[i])
	YY[i+1] = YY[i] + dt*YY[i]*(a21*XX[i]-a20) 
	XX1[i+1] = XX1[i] + dt*XX1[i]*(a10-a12*YY1[i]) + np.sqrt(XX1[i]*(a10+a12*YY1[i]))*N1
	YY1[i+1] = YY1[i] + dt*YY1[i]*(a21*XX1[i]-a20) + np.sqrt(YY1[i]*(a21*XX1[i]+a20))*N2


plt.figure(1)
plt.plot(tt,XX, linewidth=2.0, label="prey")
plt.plot(tt,YY, linewidth=2.0, label = "predator")
plt.legend(bbox_to_anchor=(1.05, 1), loc=4, borderaxespad=0.)

plt.plot(tt,XX1, 'b', linewidth=2)
plt.plot(tt,YY1, 'g', linewidth=2)
plt.legend(bbox_to_anchor=(1.05, 1), loc=4, borderaxespad=0.)
plt.show()



#plt.figure(2)
#plt.plot(tt[1:N:30],XX1[1:N:30], 'o', label="prey")
#plt.plot(tt[1:N:30],YY1[1:N:30], 'o', label = "predator")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=4, borderaxespad=0.)
#plt.show()