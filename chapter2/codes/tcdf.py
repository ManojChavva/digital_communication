import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,100)   #points on the x axis
print(x)

simlen = int(1e6)    #number of samples
print(simlen)

err = [] #declaring probability list

import subprocess
import shlex
#randvar = np.random.normal(0,1,simlen)

#randvar = np.loadtxt('uni.dat',dtype='double')
#end if

randvar = np.loadtxt('triangle.dat',dtype='double')
print(randvar)

vec_tri_cdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x**2/2, lambda x: 2*x - x**2/2 - 1, 1])
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
print(err_ind)
print(err_n)
print(err)	
plt.scatter(x.T,err,label='practical')
plt.plot(x,vec_tri_cdf,color='r',label='theory')
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])
plt.savefig('../figs/triangle_cdf.pdf')
plt.show() #opening the plot window
