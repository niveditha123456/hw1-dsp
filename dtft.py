import numpy as np;
import cmath;
from matplotlib import pyplot as plt
a=np.pi
w=np.arange(-a,a,0.01*a)
x=[1,2,3,4]
y=[]
for n in range(0,len(w)):
	s=0
	for k in range(0,len(x)):
		s=s+x[k]*np.exp(-1*1j*w[n]*k)
	y.append(s)
print(y)
plt.subplot(2,1,1)
plt.stem(w,np.abs(y));
plt.subplot(2,1,2)
plt.stem(w,np.angle(y));
plt.show()

	
	

